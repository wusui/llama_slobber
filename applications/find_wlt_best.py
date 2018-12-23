#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Find players who over the course of a season repeated the same W-L-T pattern.
"""
from operator import itemgetter
import os
import json

from llama_slobber import find_wlt_patterns
from llama_slobber import find_stored_stat
from llama_slobber import lookup_user
from llama_slobber import gen_html_page
from llama_slobber import inject_text


def find_wlt_func(_, odict):
    """
    Fucntion passed to stored stat to find wlt patterns

    Input:
        odict -- dictionary where the data will be stored
    """
    result = find_wlt_patterns(odict[1])
    return result


def action():
    """
    Scan files in match_data to find smallest wlt cycle
    """
    best = 25
    answers = {}
    result = find_stored_stat('match_data', find_wlt_func, {})
    for person in result:
        for cycle in result[person]:
            if cycle[1] < best:
                best = cycle[1]
                answers = {}
            if cycle[1] == best:
                if person in answers:
                    answers[person].append(cycle)
                else:
                    answers[person] = [cycle]
    return answers


def pat_fnd(name, value):
    """
    Arguments:
        name -- player name
        value -- ('season number', cycle-length')

    Look in match_data directory for this player and find the cycle that was
    repeated.  Return as 'W-L-T' value.
    """
    fname = "match_data" + os.sep + lookup_user('match_data', name)
    with open(fname, 'r') as pfinder:
        jstring = pfinder.read()
    info = json.loads(jstring)
    stats = info[name][1][value[0]][value[1] - 1]
    return '-'.join([str(i) for i in stats])


def lformat(info):
    """
    info is a dict indexed by player. Each value in info is a list of that
    player's best scores.  Each item in that list is a tuple containing a
    season number and the cycle size.

    This methond converts info into a list of lists suitable for display
    in a table.  The entries in that table are: name, season number,
    cycle size, and the pattern that is repeated.

    The list returned here can be used in html formatting operations.
    """
    olist = []
    for name in info:
        for value in info[name]:
            olist.append([name, int(value[0]), value[1], pat_fnd(name, value)])
    olist = sorted(olist, key=itemgetter(0))
    olist = sorted(olist, key=itemgetter(1), reverse=True)
    olist = sorted(olist, key=itemgetter(2))
    nlist = []
    for tline in olist:
        tline = [str(i) for i in tline]
        nlist.append(tline)
    return nlist


def main_routine():
    """
    Generate an html page to display Llama cycles
    """
    odata = gen_html_page({'x': lformat(action())},
                          'Llama Cycles', 'Shortest Llama Cycles',
                          centered=True,
                          tabhdrs=['Name', 'Season', 'Cycle Size',
                                   'Pattern'])
    ofile = 'generated_html' + os.sep + 'cycle_data.html'
    ifile = 'html_texts' + os.sep + 'cycle_data.txt'
    odata = inject_text(odata, ifile)
    with open(ofile, 'w') as fdesc:
        fdesc.write(odata)


if __name__ == "__main__":
    main_routine()
