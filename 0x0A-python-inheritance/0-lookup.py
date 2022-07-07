#!/usr/bin/python3
"""Module for Lookup function"""


def lookup(obj):
    """ function that returns the list of available
        attributes and methods of an object"""
    return list(dir(obj))
