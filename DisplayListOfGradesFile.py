# Importing libraries
import numpy as np
import pandas as pd

# Import other files
from FinalGradeFunction import computeFinalGrades


def displayListOfGrades(checkedDataArray: np.float64, loadedData: pd.DataFrame) -> None:
    '''
    ### If the user choose to "Display list of grades" in the main menu, this function will be called, 
    and the grades for the assignment plus the final grade will be shown.
    
    Parameters:
        - checkedDataArray (np.float64): The data in np.array format after it has been checked for errors
        - loadedData (pd.DataFrame): The original data in pd.Dataframe format, used to ascess the columns from the .csv datafile
    
    Returns:
        - None

    Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023
    '''

    # Add final grades to the data
    grades = checkedDataArray[:,2:]
    finalGrades = computeFinalGrades(grades)
    checkedDataArrayPlusFinalGrades = np.hstack((checkedDataArray, np.array([finalGrades.astype(int)]).T))

    # Sort data in alphabetic order via bubble sorting algorithm
    for x in range(len(checkedDataArrayPlusFinalGrades)):
        for y in range(len(checkedDataArrayPlusFinalGrades)):
            if y > x:
                if checkedDataArrayPlusFinalGrades[x,1] > checkedDataArrayPlusFinalGrades[y,1]:
                    t = checkedDataArrayPlusFinalGrades[x,:].copy()
                    checkedDataArrayPlusFinalGrades[x,:] = checkedDataArrayPlusFinalGrades[y,:]
                    checkedDataArrayPlusFinalGrades[y,:] = t
    
    # Make columns for data in .csv format, and convert to .csv format to make it more visually appealing
    titles = list(loadedData)
    titles = titles[::]
    titles.append('Final grade')
    
    # Print data
    print('')
    checkedDataArrayPlusFinalGrades_csv = pd.DataFrame(checkedDataArrayPlusFinalGrades) 
    checkedDataArrayPlusFinalGrades_csv.columns = titles
    print(checkedDataArrayPlusFinalGrades_csv)