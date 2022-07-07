#!/usr/bin/python3
"""Append write"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file
    Args:
        filename (str, optional): text file
        nb_lines (int, optional): must be integer
    """
    with open(filename, encoding='utf-8') as file:
        num_lines = sum(1 for line in file)

        file.seek(0)

        if nb_lines <= 0 or nb_lines >= num_lines:
            print(file.read(), end="")
            return

        i = 0
        for i in range(nb_lines):
            print(file.readline(), end="")
