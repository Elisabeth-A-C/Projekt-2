# Import libraries
import numpy as np
import math

# Import other files
from GradeRoundingFunction import roundGrade
from DataLoadFile import convertLoadedDataToGrades

def computeFinalGrades(grades):
    # Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023

    #grades = convertLoadedDataToGrades(loadedData)

    gradesFinal = np.array([])

    if grades.shape[1] == 1:
        gradesFinal = grades

    else:
        for i in range(grades.shape[0]):
            x = grades[i]

            if len(x[x < 0]) > 0:
                gradesFinal = np.concatenate((gradesFinal, np.array([-3])))
            
            else:
                minPos = np.where(x == x.min())
                if len(minPos) == len(x):
                    x = np.delete(x, minPos[0])
                gradesFinal = np.concatenate((gradesFinal, np.array([np.mean(x)])))
                gradesFinal = roundGrade(gradesFinal)

    return gradesFinal

# Test
#print(computeFinalGrades(np.array([[-3,4,7],[2,4,4],[7,10,4],[4,4,12],[10,12,12]])))