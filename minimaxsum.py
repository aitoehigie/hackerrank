#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))


result = [sum(arr[:len(arr)]) - arr[i] for i in range(len(arr))]
result.sort()

print(result[0], result[-1])
