#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Find players who over the course of a season repeated the same W-L-T pattern.
"""
from llama_slobber import find_wlt_patterns
from llama_slobber import find_stored_stat


def find_wlt_func(name, odict):
    """
    Fucntion passed to stored stat to find wlt patterns

    Input:
        name  -- player's name
        odict -- dictionary where the data will be stored
    """
    result = find_wlt_patterns(name, odict[1])
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


if __name__ == "__main__":
    print(action())
