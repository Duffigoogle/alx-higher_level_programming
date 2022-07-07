#!/usr/bin/python3
""" Text indentation """


def text_indentation(text):
    """
        prints a text with 2 new lines after
        each of these characters: ., ? and :
        Parameters:
            text: must be a string
        Raise:
            TypeError: If text is not string
        """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in [':', '.', '?']:
            print(text[i])
            print()
            i += 1
        else:
            print(text[i], end='')
        i += 1
