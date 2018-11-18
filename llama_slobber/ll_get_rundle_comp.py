#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to perform a calculation between all the members of a rundle.
"""
from operator import itemgetter
from llama_slobber.ll_rundle_members import get_rundle_members
from llama_slobber.ll_local_io import get_session
from llama_slobber.calc_hun import calc_hun
from llama_slobber.fmt_float import format_float


def get_rundle_comp(season, rundle, fsize, session_id=get_session(),
                    func_parm=calc_hun):
    """
    Perform a calculation between all members of a rundle.

    Input:
        season -- LL season number
        rundle -- rundle name "B_Pacific" for example
        fsize -- size of the field to be displayed
        func_parm -- name of the routine to be executed for all pairs in
                     this rundle.  Keyword parameter, defaults to calc_hun.

    Returns: A dictionary indexed by player name (in alphabetical order).
        Each element is a list of tuples consisting of two fields.
        The fields in the tuple are the player's opponent and caculated nunber
        based on func_parm.  These tuples are arranged in decending value
        of this func_parm number.
    """
    folks = get_rundle_members(season, rundle, session=session_id)
    result = {}
    for plyr in folks:
        result[plyr] = []
    for indx, plyr in enumerate(folks):
        for opp in folks[indx+1:]:
            hun_val = format_float(func_parm(plyr, opp, session_id=session_id),
                                   fsize)
            print(plyr, opp, hun_val)
            result[plyr].append((opp, hun_val))
            result[opp].append((plyr, hun_val))
    oresult = {}
    for plyr in sorted(folks):
        nlist = sorted(result[plyr], key=itemgetter(1), reverse=True)
        oresult[plyr] = nlist
    return oresult
