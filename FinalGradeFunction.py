# Import libraries
import numpy as np
import math

# Import other files
from GradeRoundingFunction import roundGrade
from DataLoadFile import convertLoadedDataToGrades

def computeFinalGrades(grades: np.float64) -> np.float64:
    '''
    ### Computes the final grade for each student.
    
    Parameters:
        - grades (np.float64): An array in a NxM matrix format, containing grades for each N student on M different assignments
    
    Returns:
        - gradesFinal (np.float64): An array (vector) containing the final grade for each student

    Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023
    '''

    gradesFinal = np.array([])

    # If there's only one assignment, the final grade is the grade for that assignment
    if grades.shape[1] == 1:
        gradesFinal = np.concatenate(grades) # use np.concatenate to flatten the array

    else:
        for i in range(grades.shape[0]):
            x = grades[i]

            # If one of the grades on an assignment is -3, the final grade is -3
            if len(x[x < 0]) > 0:
                gradesFinal = np.concatenate((gradesFinal, np.array([-3])))
            
            # Otherwise, the final grade is the mean of the grades on the assignments when the lowest grade is removed
            else:
                minPos = np.array([])
                minPos = np.where(x == x.min())
                x = np.delete(x, minPos[0][0])
                gradesFinal = np.concatenate((gradesFinal, np.array([np.mean(x)])))
                gradesFinal = roundGrade(gradesFinal)

    return gradesFinal

# Test
#print(computeFinalGrades(np.array([[-3,4,7],[0,4,4],[0,10,4],[4,4,12],[10,12,12]])))