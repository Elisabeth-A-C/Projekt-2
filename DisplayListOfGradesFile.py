# Importing libraries
import numpy as np
import pandas as pd

# Import other files
from FinalGradeFunction import computeFinalGrades

def displayListOfGrades(checkedDataArray, loadedData):
    grades = checkedDataArray[:,2:]
    finalGrades = computeFinalGrades(grades)
    checkedDataArrayPlusFinalGrades = np.hstack((checkedDataArray, np.array([finalGrades]).T))

    titles = list(loadedData)
    titles = titles[::]
    titles.append('Final grade')

    checkedDataArrayPlusFinalGrades = np.vstack((np.array(titles), checkedDataArrayPlusFinalGrades))

    # Sort data in alphabetic order via bubble sorting algorithm


    print('')
    print(pd.DataFrame(checkedDataArrayPlusFinalGrades)) # TO-DO: make this prettier (minus first row, and float -> int)