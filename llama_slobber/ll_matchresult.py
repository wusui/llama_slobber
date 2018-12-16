#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
# pylint: disable=E1111
"""
Handle the compilation of information for a match day.
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import MATCH_DATA
from llama_slobber.handle_conn_err import handle_conn_err


class GetMatchResult(HTMLParser):
    """
    Scan for the right match table.  Isolate player's names and the scores
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = []
        self.match = {}
        self.scan = False
        self.scandata = False

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            for apt in attrs:
                if apt[0] == 'class':
                    if apt[1] == 'tblResults':
                        self.scan = True
                        self.match = {'players': []}
        if tag == 'a':
            if not self.scan:
                return
            for apt in attrs:
                if apt[0] == 'href':
                    if apt[1].startswith('/profiles.php?'):
                        self.match['players'].append(apt[1].split('?')[1])
                        if len(self.match['players']) == 2:
                            self.result.append(self.match)
                            self.match = {'players': []}
                    if apt[1].startswith('/match.php?'):
                        self.scandata = True

    def handle_data(self, data):
        if self.scandata:
            self.match['score'] = [data[0:4], data[-4:]]

    def handle_endtag(self, tag):
        if tag == 'a':
            self.scandata = False
        if tag == 'table':
            self.scan = False


@handle_conn_err
def get_matchresult(season, day, rundle, session=get_session()):
    """
    Extract match day results

    Input:
        season -- season number
        day -- match day number in range 1 to 25
        rundle -- name of rundle (R_Pacific_Div_2, for example)

    Returns:
        A list of match results.  Each entry consists of a dictionary
        whose values are:
            players -- list of players (2 in a match)
            score -- list of corresponding match scores (strings)
    """
    page = '&'.join([str(season), str(day), rundle])
    this_url = MATCH_DATA % page
    return get_page_data(this_url, GetMatchResult(), session=session)


if __name__ == '__main__':
    XVAL = get_matchresult(78, 23, 'B_Pacific')
    print(XVAL)
