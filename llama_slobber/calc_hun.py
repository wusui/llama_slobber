#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Implement HUN number calculator
"""
from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_qhist import get_qhist
from llama_slobber.fmt_float import format_float
from llama_slobber.comp_hun import comp_hun


def calc_hun(player1, player2, session_id=None):
    """
    Calculate Hamill/Usui numbers

    Hamill/Usui numbers (HUN) are a metric to determine how similar a player
    is to another player.  This value is the number of questions on which they
    got the same result (both got right or bot missed) divided by the total
    number of questions that they answered in common.  This has a maximum
    value of one and the higher the number is, the similar to two players are.

    Parmeters:
        player1 -- first player
        player2 -- player first player is being compared to.

    Returns -- a HUN number in the range of 0 to 1.  A higher value indicates
               that the players are more 'like' each other.
    """
    if not session_id:
        session_id = get_session()
    plyr1 = get_qhist(player1, session_id)
    plyr2 = get_qhist(player2, session_id)
    return comp_hun(plyr1, plyr2)


if __name__ == "__main__":
    print(format_float(1 / 7, 6))
    print(format_float(3 / 4, 6))
    print(format_float(calc_hun('usuiw', 'veredj'), 7))
