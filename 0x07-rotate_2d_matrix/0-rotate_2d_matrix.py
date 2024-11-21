#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
from typing import List


def rotate(matrix: List[int]) -> List[int]:
    """rotates the list the wrong way LOL"""
    n = len(matrix)

    for row in matrix:
        row.reverse()

    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    return matrix


def rotate_2d_matrix(matrix: List[int]) -> List[int]:
    """rotates the matrix till it's the right way"""
    for _ in range(3):
        matrix = rotate(matrix)
    return matrix
