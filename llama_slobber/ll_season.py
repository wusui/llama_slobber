#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to extract html data to get season number
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import LLHEADER
from llama_slobber.ll_local_io import STANDINGS


class GetSeasonNumber(HTMLParser):
    """
    Parse main page to get current season number
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = ''

    def handle_starttag(self, tag, attrs):
        """
        Find first href referring to standings.php
        """
        if tag == 'a':
            if attrs[0][0] == 'href':
                if attrs[0][1].startswith(STANDINGS):
                    if self.result == '':
                        self.result = attrs[0][1].split('?')[-1]


def get_season(session=get_session()):
    """
    Find the season number

    Input:
        session request

    Returns most recent season number
    """
    return int(get_page_data(LLHEADER, GetSeasonNumber(), session=session))


if __name__ == "__main__":
    print(get_season())
