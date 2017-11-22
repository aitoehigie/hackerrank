#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A = []
    B = []
    A_score = []
    B_score = []
    A.append(a0)
    A.append(a1)
    A.append(a2)
    B.append(b0)
    B.append(b1)
    B.append(b2)
    for i, j in zip(A, B):
        if i > j:
            A_score.append(1)
        elif i < j:
            B_score.append(1)
        elif i == j:
            pass
    return (sum(A_score), sum(B_score))
    
    

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))



