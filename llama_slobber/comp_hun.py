#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Implement HUN number computations
"""


def comp_hun(plyr1, plyr2):
    """
    Do the actual computations for calc_hun.   This is broken out from
    calc_hun so that computations can be done other functions.
    """
    same = 0
    diff = 0
    for category in plyr1:
        try:
            pdata1 = plyr1[category]
            pdata2 = plyr2[category]
            for answer in pdata1['correct']:
                if answer in pdata2['correct']:
                    same += 1
                if answer in pdata2['wrong']:
                    diff += 1
            for answer in pdata1['wrong']:
                if answer in pdata2['correct']:
                    diff += 1
                if answer in pdata2['wrong']:
                    same += 1
        except KeyError:
            pass
    if diff == 0:
        diff = 1
    return same / (same + diff)
