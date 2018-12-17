#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Find patterns in the game records for a player
"""
from llama_slobber.ll_user_record import get_user_data


def find_wlt_patterns(player, pinfo):
    """
    Look for repeating patterns in the record of a player.

    Input:
        player -- player name
        pinfo -- data (from get_user_data call).
    """
    result = []
    for season in pinfo:
        if len(pinfo[season]) != 25:
            continue
        for diff in range(2, 13):
            ovec = pinfo[season][diff - 1]
            goval = True
            for tindx in range(2 * diff - 1, 25, diff):
                testv = []
                for num in range(0, 3):
                    divisor = 1
                    if ovec[num] != 0:
                        divisor = ovec[num]
                    testv.append(pinfo[season][tindx][num] / divisor)
                for num in range(1, 3):
                    if testv[num] != testv[num-1]:
                        goval = False
                        break
            if goval:
                result.append((season, diff))
    return result


def get_wlt_patterns(player):
    """
    Call get_user_data to get w-l-t record prior to calling find_wlt_patterns.
    """
    pinfo = get_user_data(player)[1]
    return find_wlt_patterns(player, pinfo)


if __name__ == '__main__':
    print(get_wlt_patterns('usuiw'))
