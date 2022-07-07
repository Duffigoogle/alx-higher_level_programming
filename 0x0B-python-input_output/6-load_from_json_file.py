#!/usr/bin/python3
"""8. Create object from a JSON file"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename (str): file that contain text
    Returns:
        object: python object
    """
    import json
    with open(filename, encoding='utf-8') as file:
        obj = json.loads(file.read())
    return obj
