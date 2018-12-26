#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Find My Own Private Scorigami values for all players
"""
from operator import itemgetter
import os

from llama_slobber import find_stored_stat
from llama_slobber import gen_html_page
from llama_slobber import inject_text


CONVLIST = [0, 1, 4, 8, 12, 15, 16]
TEXTVALUES = ['0(0)', '0(1)', '1(1)', '2(1)', '3(1)', '1(2)', '2(2)', '3(2)',
              '4(2)', '5(2)', '2(3)', '3(3)', '4(3)', '5(3)', '6(3)', '7(3)',
              '4(4)', '5(4)', '6(4)', '7(4)', '8(4)', '6(5)', '7(5)', '8(5)',
              '9(5)', '9(6)']


def find_scorigami(pinfo):
    """
    Given the matches for a player, return [x, y] where x is a list
    of missing scorigmai values, and y is matches played if x is not empty,
    or the number of games needed to  achieve scorigami if x is empty.j
    """
    scores = 26*[0]
    mcount = 0
    slist = []
    for season in pinfo:
        slist.append(int(season))
    slist = sorted(slist)
    for iseason in slist:
        season = str(iseason)
        for match in pinfo[season]:
            mcount += 1
            myscore = match[0]
            if myscore[1] < 0:
                continue
            indx = CONVLIST[myscore[1]] + myscore[0]
            scores[indx] = 1
            if sum(scores) == 26:
                return [[], mcount]
    missing = []
    for ival, indicator in enumerate(scores):
        if indicator == 0:
            missing.append(ival)
    return [missing, mcount]


def find_mops_func(odict):
    """
    Function passed to find_stored_stat to find mops values

    Input:
        odict -- dictionary extracted from match_data json

    Returns: list of ([missing values], matches)
    """
    result = find_scorigami(odict[0])
    return result


def xlate_num2score(score_indices):
    """
    Translate score indexes back into their original text.
    """
    retval = []
    for ival in score_indices:
        retval.append(TEXTVALUES[ival])
    return retval


def action():
    """
    Scan files in match_data for mops information
    """
    result = find_stored_stat('match_data', find_mops_func, {})
    new_records = []
    for person in result:
        size = len(result[person][0])
        new_records.append([person, result[person][1], size,
                            result[person][0]])
    for column in range(0, 3):
        new_records = sorted(new_records, key=itemgetter(column))
    out_list = []
    for aline in new_records:
        if aline[1] > 100:
            break
        out_list.append([aline[0], str(aline[1])])
    out_info = {}
    out_info['x'] = out_list
    odata = gen_html_page(out_info, 'MOPS', 'My Own Private Scorigami',
                          centered=True,
                          tabhdrs=['Name', 'Matches Needed'])
    ofile = 'generated_files' + os.sep + 'mops.html'
    ifile = 'html_texts' + os.sep + 'mops.txt'
    odata = inject_text(odata, ifile)
    with open(ofile, 'w') as fdesc:
        fdesc.write(odata)
    ofile = 'generated_files' + os.sep + 'mops.csv'
    with open(ofile, 'w') as cdesc:
        for record in new_records:
            csvrec = [str(i) for i in record[0:3]]
            if record[2] > 0:
                csvrec.extend(xlate_num2score(record[3]))
            cdesc.write(','.join(csvrec) + '\n')


if __name__ == "__main__":
    action()
