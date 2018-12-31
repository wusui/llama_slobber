#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Find hun values
"""
import os
import sys
from operator import itemgetter
from llama_slobber import comp_hun
from llama_slobber import lookup_user
from llama_slobber import find_stored_stat
from llama_slobber import gen_html_page
from llama_slobber import get_dir_with_field


def name_wrap(name):
    """
    Curry name so thatit can be passed to find_store_stat
    """
    def hun_act(hun_data):
        """
        Name should be curried once name_wrap is called.
        """
        return comp_hun(name, hun_data)
    return hun_act


def stringify(hun_list):
    """
    Return equivalent list with all values stringified.
    """
    olist = []
    for entry in hun_list:
        new_val = [entry[0], '{:6.5f}'.format(entry[1])]
        olist.append(new_val)
    return olist


def hun_compute(username):
    """
    Scan files in question_data and compute hun values for username
    """
    qinfo = get_dir_with_field(username, 'question_data')
    result = find_stored_stat('question_data',
                              name_wrap(qinfo[username]), {})
    new_records = []
    for person in result:
        new_records.append([person, result[person]])
    hun_list = {}
    hun_list['Lowest'] = stringify(sorted(new_records,
                                          key=itemgetter(1))[0:50])
    hun_list['Highest'] = stringify(sorted(new_records,
                                           key=itemgetter(1),
                                           reverse=True)[1:51])
    for huntype in ['Highest', 'Lowest']:
        out_info = {}
        out_info['x'] = hun_list[huntype]
        odata = gen_html_page(out_info, 'HUN',
                              '%s HUN values for %s' % (huntype, username),
                              centered=True, tabhdrs=['Name', 'HUN'])
        ofile = 'generated_files' + os.sep + '%s_HUN_for_%s.html' % (huntype,
                                                                     username)
        with open(ofile, 'w') as fdesc:
            fdesc.write(odata)
    new_records = stringify(sorted(new_records))
    ofile = 'generated_files' + os.sep + 'hun_%s.csv' % username
    with open(ofile, 'w') as fdesc:
        for record in new_records:
            fdesc.write(','.join(record) + '\n')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        hun_compute('usuiw')
    else:
        hun_compute(sys.argv[1])
