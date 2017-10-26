#!/bin/python3

import sys

def simpleArraySum(n, ar):
    ret = 0
    for num in ar:
        ret += num
    return ret

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
