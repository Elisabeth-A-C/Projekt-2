# Importing libraries
import numpy as np
import pandas as pd

# Import other files
from FinalGradeFunction import computeFinalGrades

def displayListOfGrades(checkedDataArray, loadedData):
    grades = checkedDataArray[:,2:]
    finalGrades = computeFinalGrades(grades)
    checkedDataArrayPlusFinalGrades = np.hstack((checkedDataArray, np.array([finalGrades.astype(int)]).T))

    # Sort data in alphabetic order via bubble sorting algorithm
    for x in range(len(checkedDataArrayPlusFinalGrades)):
        for y in range(len(checkedDataArrayPlusFinalGrades)):
            if y > x:
                if checkedDataArrayPlusFinalGrades[x,1] > checkedDataArrayPlusFinalGrades[y,1]:
                    t = checkedDataArrayPlusFinalGrades[x,1]
                    checkedDataArrayPlusFinalGrades[x,1] = checkedDataArrayPlusFinalGrades[y,1]
                    checkedDataArrayPlusFinalGrades[y,1] = t
    
    # Make columns for data in .csv format, and convert to .csv format to make it prettier to look at
    titles = list(loadedData)
    titles = titles[::]
    titles.append('Final grade')
    
    print('')
    checkedDataArrayPlusFinalGrades_csv = pd.DataFrame(checkedDataArrayPlusFinalGrades) 
    checkedDataArrayPlusFinalGrades_csv.columns = titles
    print(checkedDataArrayPlusFinalGrades_csv)