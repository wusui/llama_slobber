#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Common method to extract data from dictionaries stored in a directory
"""
import os
import json
from llama_slobber.lookup_user import lookup_user


def get_dir_with_field(name, indir):
    """
    Arguments:
        name -- player name
        indir -- directory with data saved.

    Lookup name in indir.  Return contents of json file that has this data.
    """
    fname = indir + os.sep + lookup_user(indir, name.lower())
    with open(fname, 'r') as pfinder:
        jstring = pfinder.read()
    return json.loads(jstring)
