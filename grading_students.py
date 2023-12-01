#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    adjusted_grades = []

    grades = list(grades)

    for grade in grades:
        if grade < 38:
            adjusted_grades.append(grade)
            continue
        elif grade % 5 == 0:
            adjusted_grades.append(grade)
            continue
        elif grade % 5 != 0:
            str_grade = str(grade)
            grade_tens = grade // 10
            
            if str_grade[1] in ['1','2','3','4']:
                closest_val = (grade_tens * 10)+5
                if (closest_val - grade) < 3:
                    adjusted_grades.append(closest_val)
                else:
                    adjusted_grades.append(grade)
            elif str_grade[1] in ['6','7','8','9']:
                closest_val = ((grade_tens+1) * 10)
                if (closest_val - grade) < 3:
                    adjusted_grades.append(closest_val)
                else:
                    adjusted_grades.append(grade)

    
    return adjusted_grades



    

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)


