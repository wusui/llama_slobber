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


class GetRundles(HTMLParser):
    """
    Parse page to find rundles listed
    """
    def __init__(self, season, league):
        HTMLParser.__init__(self)
        self.season = season
        self.league = league
        self.result = []

    def handle_starttag(self, tag, attrs):
        """
        Find all href attributes referring to standings.php
        """
        for apt in attrs:
            if apt[0] == 'href':
                if apt[1].startswith(STANDINGS):
                    parts = apt[1].split('&')
                    if '_' in parts[-1]:
                        if parts[-1].find(self.league) >= 0:
                            self.result.append(parts[-1])


def get_rundles(season, league, session=get_session()):
    """
    Get a list of rundles for the season and league specified.
    """
    main_data = LLSTANDINGS + "%d&%s" % (season, league)
    return get_page_data(main_data, GetRundles(season, league),
                         session=session)


if __name__ == "__main__":
    print(get_rundles(78, 'Pacific'))
