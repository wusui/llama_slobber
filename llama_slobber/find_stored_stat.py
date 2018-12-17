#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Scan a directory of json files and call a passed in function on each.
Save the result in a dictionary indexed by the keys used in the json files.
"""
import os
from json import loads


def find_stored_stat(directory, this_func, oresult):
    """
    Compute stats from the data saved in a directory

    Input:
        directory -- location of json files to be scanned.
        this_func -- function to be run against the entries found
        oresult -- dictionary saving the results of this_func calls
    """
    jfiles = os.listdir(directory)
    for fname in jfiles:
        ofname = "%s%s%s" % (directory, os.sep, fname)
        with open(ofname, 'r') as infile:
            odata = infile.read()
        odict = loads(odata)
        for ikey in odict:
            oresult[ikey] = this_func(ikey, odict[ikey])
    return oresult
