#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to get league names
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import STANDINGS
from llama_slobber.ll_local_io import LLSTANDINGS


class GetLeagueNames(HTMLParser):
    """
    Parse page to get current leagues
    """
    def __init__(self, season):
        HTMLParser.__init__(self)
        self.seasontag = "LL%d Leagues" % season
        self.skipsofar = True
        self.result = []

    def handle_starttag(self, tag, attrs):
        """
        Find first href referring to standings.php
        """
        if self.skipsofar:
            return
        if tag == 'a':
            if attrs[0][0] == 'href':
                if attrs[0][1].startswith(STANDINGS):
                    self.result.append(attrs[0][1].split('&')[-1])

    def handle_data(self, data):
        """
        Indicate when we should start checking
        """
        if data == self.seasontag:
            self.skipsofar = False


def get_leagues(season, session=get_session()):
    """
    Get a list of leagues for the season specified.
    """
    main_data = LLSTANDINGS + "%d" % season
    return get_page_data(main_data, GetLeagueNames(season), session=session)


if __name__ == "__main__":
    print(get_leagues(78))
    print(get_leagues(66, get_session()))
