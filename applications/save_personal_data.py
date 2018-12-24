#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
"""
Save personal data
"""
import os
import sys
import codecs
from json import dumps
from json import loads
from llama_slobber import get_season
from llama_slobber import act_on_all_rundles
from llama_slobber import get_rundle_personal
from llama_slobber import out_csv_file


def personal_by_rundle(season, rundle, payload):
    """
    Create json file of personal information for this rundle.

    Input:
        season -- season number
        rundle -- rundle name
        payload -- dictionary where 'output_directory' entry contains the
                   name of the directory where data will be stored
    """
    print(rundle, flush=True)
    outstr = dumps(get_rundle_personal(season, rundle), indent=4)
    outdir = payload['output_directory']
    fname = "%s%s%s.json" % (outdir, os.sep, rundle)
    with open(fname, "w") as ofile:
        ofile.write(outstr)


def personal_dict(season, rundle, payload):
    """
    Add to large payload dictionary.

    Input:
        season -- season number
        rundle -- rundle name
        payload -- dictionary where results will be stored
    """
    print(rundle, flush=True)
    data = get_rundle_personal(season, rundle)
    payload.update(data)


def save_personal_data(json_dir, out_dir):
    """
    Save personal data

    Input:
        out_dir -- directory where results will be stored.

    First store all the personal data into json files named by the rundle.
    Then store all the personal data into one big json file.
    """
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    season = get_season()
    files_that_exist = os.listdir(json_dir)
    if len(files_that_exist) < 5:
        act_on_all_rundles(season, personal_by_rundle,
                           {'output_directory': json_dir})
    everybody = '%s%severybody.json' % (out_dir, os.sep)
    if 'everybody.json' not in files_that_exist:
        payload = {}
        act_on_all_rundles(season, personal_dict, payload)
        outstr = dumps(payload, indent=4)
        with open(everybody, "w") as ofile:
            ofile.write(outstr)
    if 'locations.csv' not in files_that_exist:
        out_file = '%s%s%s' % (out_dir, os.sep, 'locations.csv')
        out_csv_file(out_file, everybody, 'Location')
    if 'schools.csv' not in files_that_exist:
        out_file = '%s%s%s' % (out_dir, os.sep, 'schools.csv')
        out_csv_file(out_file, everybody, 'College')
    if 'people.json' not in files_that_exist:
        with open(everybody, 'r') as infile:
            instring = infile.read()
        indata = loads(instring)
        inlist = sorted(indata.keys())
        outlist = dumps(inlist)
        with open('%s%speople.json' % (out_dir, os.sep), "w") as ofile:
            ofile.write(outlist)


if __name__ == "__main__":
    save_personal_data("personal", "generated_files")
