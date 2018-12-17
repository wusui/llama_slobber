#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Save match history for all players
"""
from json import dump
from json import loads
from llama_slobber import get_user_data


def dowrite(name1, name2, idata):
    """
    Write out a file containing a set of match data.

    Input:
        name1 -- first name in the set of data
        name2 -- last name in the set of data
        idata -- dictionary of match data
    """
    fname = "match_data/%s__%s.json" % (name1, name2)
    with open(fname, 'w') as fout:
        dump(idata, fout)


def save_match_hist():
    """
    Read personal/people.json to get players.

    For each player, call get_user_data

    Store that data in match_data files.  Each file contains 100 entries
    and are named and sorted in alphabetical order
    """
    with open('personal/people.json', 'r') as infile:
        intext = infile.read()
    indata = loads(intext)
    fname = ''
    out_data = {}
    player = ''
    for count, player in enumerate(indata):
        if count % 100 == 0:
            out_data = {}
            fname = player
        out_data[player] = get_user_data(player)
        if count == 0:
            continue
        if count % 100 == 99:
            dowrite(fname, player, out_data)
    dowrite(fname, player, out_data)


if __name__ == "__main__":
    save_match_hist()
