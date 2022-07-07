#!/usr/bin/python3
"""9. Load, add, save"""
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def add_item():
    """adds all arguments to a Python list,
    and then save them to a file
    """
    filename = "add_item.json"
    the_list = []
    try:
        the_list = load_from_json_file(filename)
    except Exception as e:
        save_to_json_file(the_list, filename)

    for i in range(1, len(sys.argv)):
        the_list.append(sys.argv[i])

    save_to_json_file(the_list, filename)


if __name__ == "__main__":
    add_item()
