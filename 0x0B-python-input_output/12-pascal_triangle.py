#!/usr/bin/python3
"""14. Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n (int): size of the Pascal’s triangle
    Returns:
        list of lists: of integers
    """

    if n <= 0:
        return list([])

    li = [[1]]

    for y in range(1, n):
        li.append([])
        for x in range(0, y + 1):
            n1 = 0
            n2 = 0
            if len(li[y - 1]) > x:
                n1 = li[y - 1][x]
            if x - 1 >= 0:
                n2 = li[y - 1][x - 1]
            li[y].append(n1 + n2)

    return li
