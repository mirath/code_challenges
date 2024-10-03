#!/bin/python3

import sys

def timeConversion(s):
    nums = list(map(int, s[:-2].split(":")))
    if s[-2:] == "PM" and nums[0] != 12:
        nums[0] += 12
    if s[-2:] == "AM" and nums[0] == 12:
        nums[0] = 0
    return ":".join(list(map('{:02}'.format, nums)))

s = input().strip()
result = timeConversion(s)
print(result)
