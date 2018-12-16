#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Find all players in a given season
"""
import sys
import codecs
from llama_slobber import get_season
from llama_slobber import get_leagues
from llama_slobber import get_rundles


def act_on_all_rundles(season, action, payload):
    """
    Act on all rundles

    Input:
        season -- season number
        action -- action we want performed on all rundles (function parameter)
        payload -- either parameters to action, or data to be returned

    The two use cases (dependig on the code in action) are:
        1. Return a large set of data -- payload will be that data
        2. Perform operations on the rundle, payload will be other input
           parameters
    """
    leagues = get_leagues(season)
    for league in leagues:
        for rundle in get_rundles(season, league):
            action(season, rundle, payload)
    return payload


def append_action(_, rundle, payload):
    """
    Simplest action case -- append rundle name to list

    Input:
        rundle -- rundle name
        payload -- list we will append rundle name to
    """
    payload.append(rundle)


if __name__ == "__main__":
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    print(act_on_all_rundles(get_season(), append_action, []))
    print(act_on_all_rundles(60, append_action, []))
