#!/usr/bin/python
# Copyright (c) 2018 Warren Usui, MIT License
# pylint: disable=W0223
"""
Implement some metrics.
"""
import math


def format_float(number, decimal_places):
    """
    Accurately round a floating-point number to the specified decimal
    places (useful for formatting results).
    """
    divisor = math.pow(10, decimal_places)
    value = number * divisor + .5
    value = str(int(value) / divisor)
    frac = value.split('.')[1]
    trail_len = decimal_places - len(frac)
    return value + ''.join(['0'] * trail_len)
