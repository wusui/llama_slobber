#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Find Pdp (players defended poorly) values for all players
"""
from operator import itemgetter
import os

from llama_slobber import find_stored_stat
from llama_slobber import stringify
from llama_slobber import gen_html_page


BAD_DEF_VALUES = [[9, 5], [8, 4], [7, 3], [5, 2], [3, 1]]


def find_oms(odict):
    """
    Look at all the scores in odict[0] and add all optimal matchday scores.
    count is indexed by the corresponding score in BAD_DEF_VALUES.  count[0]
    for example counts all 9(5) scores.  count[-1] is a sum of all the other
    count values
    """
    count = 5*[0]
    all_games = 0
    for iseason in odict[0]:
        for match in odict[0][iseason]:
            all_games += 1
            for cnt, bdv in enumerate(BAD_DEF_VALUES):
                if match[0][0] == bdv[0]:
                    if match[0][1] == bdv[1]:
                        count[cnt] += 1
    total = sum(count)
    count.append(total)
    count.append(all_games)
    return count


def averaged(list1):
    """
    List1 is a list of [name, oms-counts..., total].   Divide the oms-counts
    by the total and return in list2.
    """
    list2 = []
    for entry in list1:
        newline = [entry[0]]
        for indx in range(1, 7):
            denom = entry[7]
            if denom == 0:
                denom = 1
            newline.append(entry[indx]/denom)
        newline.append(entry[7])
        list2.append(newline)
    return list2


def str_oms_scr(column):
    """
    Given a column number, return the text of the score corresponding to
    the column
    """
    numbs = BAD_DEF_VALUES[column - 1]
    ostring = "%d(%d)" % (numbs[0], numbs[1])
    return ostring


STR_FMT = {'Total': '', 'Average': '{:7.5f}'}


def action():
    """
    Generate a csv file and a set of tables matching all optimal scores,
    totals, and averages.
    """
    result = find_stored_stat('match_data', find_oms, {})
    all_peeps = []
    for person in result:
        record = [person]
        record.extend(result[person])
        all_peeps.append(record)
    all_peeps = sorted(all_peeps, key=itemgetter(0))
    new_records = stringify(all_peeps, [])
    cfile = 'generated_files' + os.sep + 'oms.csv'
    with open(cfile, 'w') as cdesc:
        for record in new_records:
            cdesc.write(','.join(record) + '\n')
    list2 = averaged(all_peeps)
    txt_ptr = {'Total': all_peeps, 'Average': list2}
    make_html(txt_ptr)


def make_html(txt_ptr):
    """
    Generate the html page. txt_ptr contains the data extracted in action().
    """
    out_info = {}
    for tpass in ['Total', 'Average']:
        for column in range(1, 7):
            if column == 6:
                ctext = 'OMS'
            else:
                ctext = str_oms_scr(column)
            npeeps = txt_ptr[tpass]
            slist = sorted(npeeps, key=itemgetter(column), reverse=True)[0:50]
            header = "%s %s scores" % (tpass, ctext)
            nlist = []
            for entry in slist:
                nlist.append([entry[0], entry[7], entry[column]])
            fmt_list = ['', '', STR_FMT[tpass]]
            out_info[header] = stringify(nlist, fmt_list)
    odata = gen_html_page(out_info, 'OMS', 'Optimal Matchday Scores',
                          tabhdrs=[['Name', 'Matches', 'Number']])
    ofile = 'generated_files' + os.sep + 'oms.html'
    with open(ofile, 'w') as odesc:
        odesc.write(odata)


if __name__ == "__main__":
    action()
