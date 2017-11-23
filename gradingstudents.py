#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        elif grade >= 38:
            if (divmod(grade, 5)[0]*5 + 5 - grade) <= 2:
                result.append(divmod(grade, 5)[0]*5 + 5)                
            else:
                result.append(grade)
    return result
                
            
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
#print ("\n".join(map(str, result)))
for item in result:
    print (str(item))



