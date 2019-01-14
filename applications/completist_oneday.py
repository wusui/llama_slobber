#!/usr/bin/python
# Copyright (c) 2019 Warren Usui, MIT License
"""
Track all oneday participation for last year.
"""
from datetime import datetime
from operator import itemgetter

from llama_slobber import collect_onedays
from llama_slobber import ll_oneday_players


def action():
    """
    Track all oneday participation for last year.
    """
    compyear = datetime.today().year - 1
    onedays = collect_onedays(compyear)
    precs = {}
    qcount = 0
    for quiz in onedays:
        plist = ll_oneday_players(quiz)
        if plist:
            qcount += 1
        for llama in plist:
            if llama in precs:
                precs[llama] += 1
            else:
                precs[llama] = 1
    tuplelist = []
    for llama in precs:
        tuplelist.append([llama, precs[llama]])
    tuplelist = sorted(tuplelist, key=itemgetter(1), reverse=True)
    print(tuplelist)
    print(qcount)


if __name__ == "__main__":
    action()
