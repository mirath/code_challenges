#!/bin/python3

import sys
from itertools import islice

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

def axel_it(A, m, n):
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

def following(pos, A, m, n):
    if pos[0] < m-A-1 and pos[1] == A:
        return (pos[0]+1,pos[1])

    if pos[0] == m-A-1 and pos[1] < n-A-1:
        return (pos[0],pos[1]+1)

    if pos[0] > A and pos[1] == n-A-1:
        return (pos[0]-1,pos[1])

    if pos[0] == A and pos[1] > A:
        return (pos[0],pos[1]-1)

def nth(th, A, m, n):
    p=(A,A)
    while th > 0:
        p=following(p, A, m, n)
    return p

