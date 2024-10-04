#!/usr/bin/python3
"""
pacal's triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    if n == 1:
        return [1]
    if n == 2:
        return [[1], [1, 1]]
    retlist = [[1], [1, 1]]
    for i in range(2, n):
        newlist = [1]
        for j in range(1, i):
            newlist.append(retlist[i - 1][j] + retlist[i - 1][j - 1])
        newlist.append(1)
        retlist.append(newlist)
    return retlist
