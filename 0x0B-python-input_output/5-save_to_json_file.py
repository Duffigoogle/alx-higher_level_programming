#!/usr/bin/python3
"""7. Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj (object): a python object
        filename (str): name of the json file
    """
    import json

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
