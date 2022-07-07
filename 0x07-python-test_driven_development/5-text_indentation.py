#!/usr/bin/python3
"""4. Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of
    these characters: ., ? and :
    Parameters:
        text: must be a string
    Raises:
        TypeError: If text is not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    is_omitting_spaces = False
    for c in text:
        if is_omitting_spaces and c is " ":
            continue
        if c in [".", "?", ":"]:
            print("{}\n".format(c))
            is_omitting_spaces = True
        else:
            print(c, end="")
            is_omitting_spaces = False
