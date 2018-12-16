#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
# pylint: disable=E1111
"""
Get the number of matches played in the current season.
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import ARUNDLE
from llama_slobber.ll_season import get_season
from llama_slobber.handle_conn_err import handle_conn_err


class GetCurrentlyFinishedCount(HTMLParser):
    """
    Scan the Match Day table for completed matches
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.right_table = False
        self.result = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            for apt in attrs:
                if apt[0] == 'class':
                    if apt[1] == 'MDTable':
                        self.right_table = True
        if tag == 'a':
            if self.right_table:
                for apt in attrs:
                    if apt[0] == 'href':
                        if apt[1].startswith('/match.php'):
                            self.result += 1

    def handle_endtag(self, tag):
        if tag == 'table':
            self.right_table = False


@handle_conn_err
def get_matchcount(session=get_session()):
    """
    Find matches in current season

    Input:
        session request

    """
    return get_page_data(ARUNDLE % (get_season(), 'Pacific'),
                         GetCurrentlyFinishedCount(), session=session)


if __name__ == '__main__':
    print(get_matchcount())
