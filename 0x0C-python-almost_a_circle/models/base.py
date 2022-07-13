#!/usr/bin/python3
"""Module for Base class"""
from json import dumps, loads
import csv
from os import path


class Base:
    """This is a “base” class of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
