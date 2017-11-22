#!/bin/python3

import sys


n = int(input().strip())
index = 1
space_start = n - 1
hash_start = 1
for i in range(n):
    print (" " * space_start + "#" * hash_start)
    space_start -= 1
    hash_start += 1
