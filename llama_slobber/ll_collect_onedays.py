#!/usr/bin/python
# Copyright (c) 2019 Warren Usui, MIT License
# pylint: disable=W0223
# pylint: disable=E1111
"""
Collect one day quiz names
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import ONEDAYS
from llama_slobber.handle_conn_err import handle_conn_err


ONEDAY_TXT = '/oneday'
O_INFO = len(ONEDAY_TXT)


class GetOneDayQuiz(HTMLParser):
    """
    Scan the Match Day table for completed matches
    """
    def __init__(self, year):
        HTMLParser.__init__(self)
        self.year = year
        self.result = []
        self.candidate = ''

    def handle_starttag(self, tag, attrs):
        for apt in attrs:
            if apt[0] == 'href':
                if apt[1].startswith(ONEDAY_TXT):
                    oinfo = apt[1][O_INFO:]
                    if oinfo in ['/rules.php', '/onedaysalpha.php']:
                        continue
                    if oinfo.startswith('.php?'):
                        self.candidate = oinfo.split('?')[-1]
                    if oinfo.startswith('/'):
                        self.candidate = oinfo[1:].split('.')[0]

    def handle_data(self, data):
        if not self.candidate:
            return
        if self.year == -1:
            self.result.append(self.candidate)
            self.candidate = ''
            return
        if data.find(', ') > 0:
            ldate = data.split(' ')[-1]
            try:
                tyear = int(ldate)
            except ValueError:
                return
            if tyear == self.year:
                self.result.append(self.candidate)
                self.candidate = ''
                return

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.candidate = ''


@handle_conn_err
def collect_onedays(year=-1, session=get_session()):
    """
    Year is a keyword argument.  Default is collect all.
    """
    return get_page_data(ONEDAYS, GetOneDayQuiz(year), session=session)


if __name__ == '__main__':
    print(collect_onedays())
