#!/usr/bin/python3
"""
Defines a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """
    Check if n is less than or equal to 0, return an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)
    return triangle
