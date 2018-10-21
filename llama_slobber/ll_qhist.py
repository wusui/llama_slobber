#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Function used to get a players question history
"""
from html.parser import HTMLParser

from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import get_page_data
from llama_slobber.ll_local_io import QHIST


class GetQhist(HTMLParser):
    """
    Parse page to find question history
    """
    def __init__(self, player):
        HTMLParser.__init__(self)
        self.player = player
        self.getkey = False
        self.lastq = ''
        self.category = ''
        self.result = {}

    def handle_starttag(self, tag, attrs):
        """
        'liclosed' indicates a new category is coming up
        'hrefs' to questions indicated a question
        'greendot.gif' is correct, 'reddot.gif' is incorrect.
        """
        for apt in attrs:
            if apt[0] == 'class':
                if apt[1] == 'liclosed':
                    self.getkey = True
            if apt[0] == 'href':
                if apt[1].startswith('/question.php'):
                    parts = apt[1].split('?')
                    qvals = parts[1].split('&')
                    self.lastq = '-'.join(qvals)
            if apt[0] == 'src':
                if apt[1].startswith('/images/misc/'):
                    lptr = self.result[self.category]
                    if apt[1].endswith('greendot.gif'):
                        lptr['correct'].append(self.lastq)
                    if apt[1].endswith('reddot.gif'):
                        lptr['wrong'].append(self.lastq)

    def handle_data(self, data):
        """
        Get new category name
        """
        if self.getkey:
            self.result[data] = {'correct': [], 'wrong': []}
            self.category = data
            self.getkey = False


def get_qhist(player, session=get_session()):
    """
    Extract player's question history.

    Returns a dict indexed by categories.  Each dict entry consists
    of a 'correct' list and a 'wrong' list of questions asked.
    """
    main_data = QHIST % player.lower()
    return get_page_data(main_data, GetQhist(player), session=session)


if __name__ == "__main__":
    print(get_qhist('UsuiW'))
