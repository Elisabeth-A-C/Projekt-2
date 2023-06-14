import numpy as np
import math

def roundGrade(grades):
    # Round up if the grade is right in between two grades.
    # Author: Filip
    i = 0
    while i < len(grades):
        if grades[i] >= 11:
            grades[i]=12
        elif grades[i] >= 8.5 and grades[i] < 11:
            grades[i]=10
        elif grades[i] >= 5.5 and grades[i] < 8.5:
            grades[i]=7
        elif grades[i] >= 3 and grades[i] < 5.5:
            grades[i]=4
        elif grades[i] >= 1 and grades[i] < 3:
            grades[i]=2
        elif grades[i] >= -1.5 and grades[i] < 1:
            grades[i]=0
        elif grades[i] < -1.5:
            grades[i]=-3
        i+=1
    gradesRounded = grades
    return gradesRounded

# Test
#inp = np.random.uniform(-3, 12, 10)
#print(roundGrade(inp))