#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Handle Local I/O and global definitions

INPUTDATA (logindata.ini) is a local file that controls what happens here.

In the DEFAULT section of INPUTDATA, the following must be defined:
    username -- a valid LL name
    password -- the LL password corresponding to username
"""
import configparser
import requests

LLHEADER = 'https://www.learnedleague.com'
LOGINFILE = LLHEADER + '/ucp.php?mode=login'
USER_DATA = LLHEADER + '/profiles/previous.php?%s'
QHIST = LLHEADER + '/profiles/qhist.php?%s'
MATCH_DATA = LLHEADER + '/match.php?%s'
ONEDAYS = LLHEADER + '/oneday'
STANDINGS = '/standings.php?'
LLSTANDINGS = LLHEADER + STANDINGS
ARUNDLE = LLSTANDINGS + '%d&A_%s'
INPUTDATA = 'logindata.ini'


def get_session():
    """
    Read an ini file, establish a login session

    Input:
        inifile -- name of local ini file with control information

    Returns: logged in requests session to be used in later operations
    """
    config = configparser.ConfigParser()
    config.read(INPUTDATA)
    payload = {'login': 'Login'}
    for attrib in ['username', 'password']:
        payload[attrib] = config['DEFAULT'][attrib]
    ses1 = requests.Session()
    try:
        loginfile = config['DEFAULT']['loginfile']
    except KeyError:
        loginfile = LOGINFILE
    ses1.post(loginfile, data=payload)
    return ses1


def get_page_data(url, parser, session=get_session()):
    """
    Extract data from a url

    Input:
        url -- url we are extracting data from
        parser -- http parser that collects the data to be extracted
        session -- results login session

    Returns:
        data collected by parser
    """
    main_data = session.get(url)
    parser1 = parser
    parser1.feed(main_data.text)
    return parser1.result
