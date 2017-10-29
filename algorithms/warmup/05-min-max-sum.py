#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

arr.sort()

min=sum(arr[:4])
max=sum(arr[1:])

print("%s %s"%(min, max))
