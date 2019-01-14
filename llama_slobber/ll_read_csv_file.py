#!/usr/bin/python
# Copyright (c) 2019 Warren Usui, MIT License
"""
Csv file reader, and one-day utilities (one-day data is the most common
use of csv files by Learned League).
"""
from llama_slobber.ll_local_io import get_session
from llama_slobber.ll_local_io import LLHEADER


def get_csv_oneday_players(quiz, session=get_session()):
    """
    Return a list of Llamas who participated in the indicated one-day quiz.
    """
    results = get_csv_oneday_data(quiz, session=session)
    retval = []
    for data in results:
        retval.append(data[0])
    return retval


def get_csv_oneday_data(quiz, session=get_session()):
    """
    Given a quiz name, return the csv file for that quiz.
    """
    httpv = "%s/oneday/csv/%s.csv" % (LLHEADER, quiz)
    return read_csv_data(httpv, session=session)


def read_csv_data(url, session=get_session()):
    """
    Read a csv file pointed to by a url.  Return a list of lines.  Each
    line is a list of fields.
    """
    main_data = session.get(url)
    flines = main_data.text.strip().split('\n')
    retval = []
    for peep in flines[1:]:
        newpeep = peep.split(',')
        retval.append(newpeep[1:])
    return retval


if __name__ == "__main__":
    print(get_csv_oneday_players("mit"))
