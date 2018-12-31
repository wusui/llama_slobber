#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Find a text entry inside an alphabetically arranged list of json files.
"""
import os


SPLITTER_IN_DICTNAMES = '___'


def get_wbounds(lookup_fname):
    """
    When the text is "foo___bar.json", return ['foo', 'bar']
    """
    vtext = lookup_fname.split('.')[0]
    return vtext.split(SPLITTER_IN_DICTNAMES)


def lookup_user(directory, in_text):
    """
    Lookup a user in a set up files.

    Arguments:
       directory -- directory where every file name has the form "x___y.json"
                    x and y are alphabetically ordered entries, and every
                    entry in that file is within the range of x and y.
       in_text -- text to scan for.
    """
    in_text = in_text.lower()
    list_to_srch = sorted(os.listdir(directory))
    left = 0
    right = len(list_to_srch) - 1
    midpoint = (left + right) // 2
    while left != midpoint:
        found = False
        if in_text < get_wbounds(list_to_srch[midpoint])[0]:
            right = midpoint
            found = True
        if in_text > get_wbounds(list_to_srch[midpoint])[1]:
            left = midpoint
            found = True
        if not found:
            return list_to_srch[midpoint]
        midpoint = (left + right) // 2
    if in_text > get_wbounds(list_to_srch[midpoint])[1]:
        return list_to_srch[right]
    return list_to_srch[midpoint]


if __name__ == "__main__":
    print(lookup_user("../applications/match_data", 'usuiw'))
