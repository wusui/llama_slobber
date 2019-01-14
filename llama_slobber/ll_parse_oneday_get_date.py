#!/usr/bin/python
# Copyright (c) 2019 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to find the date of a oneday.
"""
from html.parser import HTMLParser
from datetime import date
from datetime import datetime
from datetime import timedelta

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import ONEDAYS
from llama_slobber.handle_conn_err import handle_conn_err


class GetDateFromUrl(HTMLParser):
    """
    Parse page to get date of this oneday.
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.result = ''
        self.scanflag = False

    def handle_starttag(self, tag, attrs):
        """
        find matchday indicator
        """
        if tag == 'h1':
            for apt in attrs:
                if apt[0] == 'class':
                    if apt[1] == 'matchday':
                         self.scanflag = True

    def handle_data(self, data):
        """
        Get date if available
        """
        if self.scanflag:
            self.result = data
            self.scanflag = False


@handle_conn_err
def parse_oneday_get_date(oneday, session=get_session()):
    """
    Find the date of a oneday event.

    Returns a date value
    """
    urlv = "%s.php?%s" % (ONEDAYS, oneday)
    one_day_str = get_page_data(urlv, GetDateFromUrl(), session=session)
    extract = one_day_str.strip()
    if not extract:
        return date.today() + timedelta(days=1)
    extdate = extract.split(':')[0]
    return datetime.strptime(extdate, "%B %d, %Y").date()


if __name__ == "__main__":
    print(parse_oneday_get_date('classic_79'))
    print(parse_oneday_get_date('mit'))
    print(parse_oneday_get_date('indy500'))
    print(parse_oneday_get_date('philiproth'))
    print(parse_oneday_get_date('skiing'))
    print(parse_oneday_get_date('42'))
    print(parse_oneday_get_date('aardvarkx'))
