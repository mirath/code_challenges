#!/bin/python3

import sys
import queue
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

def rotate_axel(r, A, m, n, matrix):
    p=(A,A)
    q = queue.Queue()
    elements = 2*(m-2*A) + 2*(n-2-2*A)
    r = r % elements

    if r == 0:
        return matrix

    while r > 0:
        q.put(matrix[p[0]][p[1]])
        p=following(p, A, m, n)
        r -= 1

    i = elements
    while i > 0:
        val = q.get(False)
        q.put(matrix[p[0]][p[1]])
        matrix[p[0]][p[1]] = val
        p=following(p, A, m, n)
        i -= 1

    return matrix

def rotate(shift, m, n, matrix):
    axels = int(min(m, n) / 2)
    for a in range(axels):
        rotate_axel(shift, a, m, n, matrix)
    return matrix


matrix, m, n, r = io()
rotate(r, m, n, matrix)
for row in matrix:
    print(" ".join(map(str, row)))

