#!/bin/python3

import sys
precision = 6


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = []
neg = []
zero = []

for _, item in enumerate(arr):
    if item > 0:
        pos.append(item)
    elif item == 0:
        zero.append(item)
    elif item < 0:
        neg.append(item)

  
positives = len(pos)/len(arr)
negatives = len(neg)/len(arr)
zeros = len(zero)/len(arr)

print(positives)
print(negatives)
print(zeros)
