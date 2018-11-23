#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Implement WONDER calculator.
"""
from operator import itemgetter
from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import TOTAL_MATCHES_PER_SEASON
from llama_slobber.ll_season import get_season
from llama_slobber.ll_matchcount import get_matchcount
from llama_slobber.ll_matchresult import get_matchresult
from llama_slobber.ll_rundle_members import get_rundle_personal


def comp_diff(scores):
    """
    Return a single numeric index that represents how the scores relate
    relative to wonder values.  This index is used in calc_wonder to
    find a wonder value.
    """
    if 'F' in scores[0] or 'F' in scores[1]:
        return 0
    indx = 0
    for char in range(0, 3, 2):
        numb0 = int(scores[0][char])
        numb1 = int(scores[1][char])
        val = 1
        if numb0 > numb1:
            val = 2
        if numb0 < numb1:
            val = 0
        indx *= 3
        indx += val
    return indx


def match_anal(match_res):
    """
    Reorganize match_res values into a single list with the score being
    set by a call to comp_diff
    """
    return [match_res['players'][0], match_res['players'][1],
            comp_diff(match_res['score'])]


def calc_wonder(season, rundle, session_id=None):
    """
    Calculate a season's worth of WONDER values for a rundle.

    WONDER ("Warren's Overtly Narcissistic Defensive Efficiency Rating") is a
    statistic that measures how much defense affected the standings points
    of a player.  It compares match point scores with total questions scores
    for a match.  If player A and player B tie on total questions but player A
    beats player B on matchpoints, then player A's WONDER score goes up by 1
    and player B's WONDER score goes down by 1.  Similarly, a loss in total
    questions with a tie in matchpoints would also change WONDER values by 1,
    and a loss in total questions with a win in matchpoints would change
    WONDER values by 2.

    Since this value only changes by a low integer, the tracking of this
    value is only being done for each season.

    Parameters:
        season -- season number
        rundle -- name of rundle (R_Pacific_Div_2, for example)

    Returns -- a list of two item lists whose values are the name of a person
               and the corresponding WONDER values accumlated for the
               entire season
    """
    wonderv = [0, -1, -2, 1, 0, -1, 2, 1, 0]
    if not session_id:
        session_id = get_session()
    current_season = get_season(session_id)
    if season == current_season:
        match_count = get_matchcount(session_id)
    else:
        match_count = TOTAL_MATCHES_PER_SEASON
    pdata = get_rundle_personal(season, rundle)
    players = {}
    for plyr in pdata:
        players[plyr] = 0
    for day in range(0, match_count):
        for match_res in get_matchresult(season, day+1, rundle):
            results = match_anal(match_res)
            players[results[0]] += wonderv[results[2]]
            players[results[1]] -= wonderv[results[2]]
    output = []
    for oplyr in sorted(players.keys()):
        output.append([oplyr, players[oplyr]])
    output = sorted(output, key=itemgetter(1), reverse=True)
    for entry in output:
        entry[1] = str(entry[1])
    return output


if __name__ == "__main__":
    print(calc_wonder(78, 'B_Pacific'))
