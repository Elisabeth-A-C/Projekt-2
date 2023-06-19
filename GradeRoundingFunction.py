# Importing libraries
import numpy as np
import math

def roundGrade(grades: np.float64) -> np.float64:
    # Round up if the grade is right in between two grades.
    # Otherwise the function will round any number in a vector to the nearest number on the 7-step scale.
    # Author: Filip Pisinger, s224072@dtu.dk, 2023
    i = 0
    while i < len(grades):
        if grades[i] >= 11:
            grades[i]=12
        elif grades[i] >= 8.5:
            grades[i]=10
        elif grades[i] >= 5.5:
            grades[i]=7
        elif grades[i] >= 3:
            grades[i]=4
        elif grades[i] >= 1:
            grades[i]=2
        elif grades[i] >= -1.5:
            grades[i]=0
        elif grades[i] < -1.5:
            grades[i]=-3
        i+=1
    gradesRounded = grades
    return gradesRounded
