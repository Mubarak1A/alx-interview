#!/usr/bin/python3
"""Module of pascal_triangle function"""
def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n:
       Returns an empty list if n <= 0
       assume n will be always an integer
    """
    if n <= 0:
        return []

    triangle_list  = [[1]]

    for i in range(1, n):
        prev_row = triangle_list[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle_list.append(new_row)

    return triangle_list
