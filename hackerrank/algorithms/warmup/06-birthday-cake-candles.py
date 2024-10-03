#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    mx = 0
    cnt = 0
    for i in ar:
        if i > mx:
            mx = i
            cnt = 1
            continue
        if i == mx:
            cnt += 1

    return cnt

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
