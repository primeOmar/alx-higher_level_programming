#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for line in matrix:
        square.append([c**2 for c in line])
    return square
