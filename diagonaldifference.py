#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    
l = []
r = []

l_starting_index = 0
r_starting_index = -1

for item in a:
    l.append(item[l_starting_index])
    l_starting_index += 1
    continue
    
for item in a:
    r.append(item[r_starting_index])
    r_starting_index -= 1
    continue
    
print (abs(sum(l)-sum(r)))
    
    
