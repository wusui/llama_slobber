#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Extract json data and put in cvs file
"""
from json import loads


def out_csv_file(out_csv, in_json, field):
    """
    Generate a csv file from information stored locally

    Input:
        out_csv  -- file csv will be written to
        in_json -- file with data to be extacted
        field -- field to be extracted
    """
    olist = []
    with open(in_json, "r", encoding='utf-8') as ifile:
        rdata = loads(ifile.read())
        for ikey in rdata:
            if rdata[ikey]:
                if not field:
                    ostring = ikey + ',' + ','.join(rdata[ikey])
                else:
                    if field in rdata[ikey]:
                        ostring = ikey + ',' + rdata[ikey][field]
                    else:
                        ostring = ikey
                olist.append(ostring)
    olist = sorted(olist)
    odata = '\n'.join(olist)
    with open(out_csv, "w", encoding='utf-8') as ofile:
        ofile.write(odata + '\n')
