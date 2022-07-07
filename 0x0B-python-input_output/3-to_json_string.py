#!/usr/bin/python3
"""5. To JSON string"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj: python object
    Returns:
        [str]: JSON representation
    """
    import json
    return json.dumps(my_obj)
