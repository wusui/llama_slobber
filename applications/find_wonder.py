#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Find players who over the course of a season repeated the same W-L-T pattern.
"""
from operator import itemgetter
import os

from llama_slobber import score_wonder
from llama_slobber import find_stored_stat
from llama_slobber import gen_html_page


def find_wonder(pinfo):
    """
    Given the matches for a player, return [x, y] where x is the
    wonder number and y is the total number of matches.
    """
    result = [0, 0]
    for season in pinfo:
        for match in pinfo[season]:
            result[0] += score_wonder(match)
            result[1] += 1
    return result


def find_wonder_func(odict):
    """
    Fucntion passed to find_stored_stat to find wonder numbers

    Input:
        odict -- dictionary extracted from match_data json

    Returns: list of (wonder, total matches)
    """
    result = find_wonder(odict[0])
    return result


def stringify(wonder_list):
    """
    Return equivalent list with all values stringified.
    """
    olist = []
    for entry in wonder_list:
        new_val = [entry[0], str(entry[1]), str(entry[2]),
                   '{:7.5f}'.format(entry[3])]
        olist.append(new_val)
    return olist


def action():
    """
    Scan files in match_data to wonder value extremes
    """
    result = find_stored_stat('match_data', find_wonder_func, {})
    new_records = []
    for person in result:
        if result[person][1] == 0:
            continue
        ratio = result[person][0] / result[person][1]
        new_records.append([person, result[person][1],
                            result[person][0], ratio])
    new_records = sorted(new_records, key=itemgetter(0))
    wwon_list = sorted(new_records, key=itemgetter(2))[0:50]
    bwon_list = sorted(new_records, key=itemgetter(2), reverse=True)[0:50]
    wav_list = sorted(new_records, key=itemgetter(3))[0:50]
    bav_list = sorted(new_records, key=itemgetter(3), reverse=True)[0:50]
    out_info = {}
    out_info['highest wonder values'] = stringify(bwon_list)
    out_info['lowest wonder values'] = stringify(wwon_list)
    out_info['highest wonder average'] = stringify(bav_list)
    out_info['lowest wonder average'] = stringify(wav_list)
    odata = gen_html_page(out_info, 'Wonder Numbers', 'Wonder Numbers',
                          tabhdrs=[['Name', 'Matches', 'Wonder', 'Average']])
    ofile = 'generated_files' + os.sep + 'wonder.html'
    with open(ofile, 'w') as fdesc:
        fdesc.write(odata)
    new_records = stringify(new_records)
    cfile = 'generated_files' + os.sep + 'wonder.csv'
    with open(cfile, 'w') as cdesc:
        for record in new_records:
            cdesc.write(','.join(record) + '\n')


if __name__ == "__main__":
    action()
