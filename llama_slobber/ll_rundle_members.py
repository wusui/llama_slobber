#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to find members of a rundle.
"""
from html.parser import HTMLParser
from json import dumps

from llama_slobber.ll_personal_data import get_personal_data
from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import LLHEADER


class GetRundleMembers(HTMLParser):
    """
    Parse rundle page to get players
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.lname = ''
        self.notlogin = False
        self.result = []

    def handle_starttag(self, tag, attrs):
        """
        Find player reference
        """
        if tag == 'a':
            for apt in attrs:
                if apt[0] == 'href':
                    if apt[1].startswith('/profiles.php'):
                        self.lname = apt[1].split('?')[1]
                if apt[0] == 'class':
                    if apt[1] == 'flag':
                        self.notlogin = True

    def handle_endtag(self, tag):
        if tag == 'a':
            if self.notlogin:
                self.result.append(self.lname)
        self.notlogin = False
        self.lname = ''


def get_rundle_members(season, rundle, session=get_session()):
    """
    Get players in a rundle

    Input:
        season -- season number
        rundle -- rundle name (B_Pacific, for example)
        session request

    Returns list of user names of players in the rundle
    """
    page = "%s/standings.php?%d&%s" % (LLHEADER, season, rundle)
    return get_page_data(page, GetRundleMembers(), session=session)


def get_rundle_personal(season, rundle, session=get_session()):
    """
    Call get_personal_data on all members of a rundle.

    Input:
        season -- season number
        rundle -- rundle name (B_Pacific, for example)
        session request

    Return personal info in a dictionary indexed by person.
    """
    retv = {}
    plist = get_rundle_members(season, rundle, session=session)
    for person in plist:
        retv[person] = get_personal_data(person, session)
    return retv


if __name__ == "__main__":
    print(dumps(get_rundle_personal(78, 'B_Pacific'), indent=4))
