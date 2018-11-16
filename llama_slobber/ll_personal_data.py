#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to find personal info.
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import LLHEADER


def find_info(person, data, field):
    """
    Parse a llama's page for metadata

    Input:
        person -- dictionary of personal data for this llama
        data -- partial text of a person page
        field -- data we are looking for
    """
    position = data.find(field+':')
    if position > -1:
        value = data[position:].split(':')[1].split('\n')[0].strip()
        person[field] = value


class GetPersonalInfo(HTMLParser):
    """
    Parse profile page.
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsetext = False
        self.result = {}

    def handle_starttag(self, tag, attrs):
        """
        Find personal data
        """
        if tag == 'p':
            for apt in attrs:
                if apt[0] == 'class':
                    if apt[1].startswith('close'):
                        self.parsetext = True

    def handle_data(self, data):
        if self.parsetext:
            for field in ['Gender', 'Location', 'College']:
                find_info(self.result, data, field)

    def handle_endtag(self, tag):
        if tag == 'p':
            self.parsetext = False


def get_personal_data(person, session=get_session()):
    """
    Get information on a person

    Input:
        person -- LL id.
        session request

    Returns: dictionary of user's metadata (Location, Gender, College)
    """
    page = "%s/profiles.php?%s" % (LLHEADER, person)
    return get_page_data(page, GetPersonalInfo(), session=session)


if __name__ == "__main__":
    print(get_personal_data('usuiw'))
