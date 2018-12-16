#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
# pylint: disable=E1111
"""
Get the scores and w-L-T records of all matches for a player
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import USER_DATA
from llama_slobber.handle_conn_err import handle_conn_err


class GetUserData(HTMLParser):
    """
    Scan the Match Day table for completed matches
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.right_table = False
        self.result = [{}, {}]
        self.season = 0

    def handle_data(self, data):
        if data.startswith("LL"):
            snumb = data.split(' ')[0]
            self.season = int(snumb[2:])
            self.result[0][self.season] = []
            self.result[1][self.season] = []
        else:
            if data.find(')-') > 0:
                nscore = []
                sparts = data.split('-')
                for part in sparts:
                    chr2 = part[2]
                    if chr2 == 'F':
                        chr2 = '-1'
                    sval = [int(part[0]), int(chr2)]
                    nscore.append(sval)
                self.result[0][self.season].append(nscore)
            else:
                parts = data.split('-')
                if len(parts) == 3:
                    wlrecs = []
                    for wlpart in parts:
                        wlrecs.append(int(wlpart))
                    self.result[1][self.season].append(wlrecs)


@handle_conn_err
def get_user_data(player, session=get_session()):
    """
    Return information about a user:
        Tuple of two dicts:
            first Dict -- indexed by season, list of scores as 2 x 2 tuples.
            second Dict -- indexed by season, list of W-L-T records as tuples
        All values are integers

    Input:
        player -- player name
        session request
    """
    return get_page_data(USER_DATA % player, GetUserData(), session=session)


if __name__ == '__main__':
    print(get_user_data('usuiw')[1][78])
