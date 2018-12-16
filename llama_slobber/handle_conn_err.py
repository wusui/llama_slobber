#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Several long running tasks to scrape data would not finish due
to connection errors.  This wrapper function is used to decorate
functions so that they retry after ConnectionError failures.
"""
import requests


def handle_conn_err(func):
    """
    Connection tester wrapper caller

    Input:
        func -- function to be wrapped
    """
    def func_wrapper(*args, **kwargs):
        """
        If the function call works, exit return the functions return value.
        Otherwise try again for at most 10 tries.  In my experience, this
        only ends up retrying once in almost all casses.
        """
        for _ in range(0, 10):
            try:
                return func(*args, **kwargs)
            except requests.ConnectionError as conn_err:
                print(conn_err)
        return None
    return func_wrapper
