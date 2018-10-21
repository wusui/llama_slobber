#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to extract html data to get oneday information
"""
from html.parser import HTMLParser
from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import ONEDAYS


class GetOnedayInfo(HTMLParser):
    """
    Parse page to get oneday info back unitl March 2012 (format change in
    link name is not handled by this code.
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = []
        self.state = 0
        self.incell = False
        self.stopped = True
        self.label = ''
        self.name = ''

    def handle_starttag(self, tag, attrs):
        if self.stopped:
            return
        if tag == 'td':
            self.incell = True
        if tag == 'a':
            if attrs[0][0] == 'href':
                if attrs[0][1].startswith('/oneday.php?'):
                    parts = attrs[0][1].split('?')
                    self.label = parts[1]
                    self.state = 1

    def handle_data(self, data):
        if data == 'Past One-Days':
            self.stopped = False
        if self.stopped:
            return
        if self.incell:
            if self.state == 2:
                self.result.append([data, self.label, self.name])
                self.state = 0
            if self.state == 1:
                self.name = data
                self.state = 2

    def handle_endtag(self, tag):
        if tag == 'td':
            self.incell = False


def get_onedays(session=get_session()):
    """
    Get oneday records from ONEDAYS page
    """
    return get_page_data(ONEDAYS, GetOnedayInfo(), session=session)


if __name__ == "__main__":
    X = get_onedays()
    print(X)
