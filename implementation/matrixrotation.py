#!/bin/python3

import sys

test_m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def io():
    lst = list(map(int, input().strip().split(' ')))
    m = lst[0]
    n = lst[1]
    r = lst[2]

    matrix = []
    i = 0
    while i < m:
        matrix.append(list(map(int, input().strip().split(' '))))
        i += 1
    return matrix,m,n,r

def axel_it(A, m, n, matrix):
    i = A
    j = A
    while i < m-A-1:
        yield i,j
        i += 1

    while j < n-A-1:
        yield i,j
        j += 1

    while i > A:
        yield i,j
        i -= 1

    while j > A:
        yield i,j
        j -= 1
