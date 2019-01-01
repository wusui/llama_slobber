#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Make sure all elements in a list are strings.  Format floats if you want.
"""


def stringify(in_fields, formats):
    """
    Arguments:
        in_fields -- list of lists to stringify
        formats -- list of correspoding formats
    """
    olist = []
    for entry in in_fields:
        new_val = []
        for indx, part in enumerate(entry):
            if indx >= len(formats):
                new_val.append(str(part))
            else:
                if formats[indx]:
                    new_val.append(formats[indx].format(part))
                else:
                    new_val.append(str(part))
        olist.append(new_val)
    return olist
