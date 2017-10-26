#!/bin/python3

import sys


n = int(input().strip())

for i in range(n):
    step = " "*(n-i-1) + "#"*(i+1)
    print(step)
