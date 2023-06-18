# Importing libraries
import numpy as np
import pandas as pd
import math

# Import other files
from DataLoadFile import dataLoad
from DataLoadFile import convertLoadedDataToGrades
from GradeRoundingFunction import roundGrade

# Import function used for global variables
import globalVariablesFile as g

def checkErrors(loadedData: pd.DataFrame) -> np.float64:
    '''
    ### If the user choose to "Check for data errors" in the main menu, this function will be called, 
    the data will be checked for two types of errors: 
        1) student duplicants
        2) grade numbers that doesn't exist on the 7-step grading scale.
    
    Parameters:
        - loadedData (pd.DataFrame): The original data in pd.Dataframe format
    
    Returns:
        - loadedDataArray (np.float64): The data in np.array format after it has been checked for errors

    Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023
    '''

    ## First check if the studentID is a duplicant, and delete the duplicants ##

    # loadedData as an np.array
    loadedDataArray = np.array(loadedData)

    # Array containing studentID for each student
    studentIDArray = np.array(loadedData.StudentID)

    # Remove duplicates
    newStudentIDArray = np.array([])
    listOfOtherDuplicants = list() # to delete

    print('')

    # If the studentID is not in the newStudentIDArray, add it to the array
    for i in range(np.size(studentIDArray)):
        if studentIDArray[i] not in " ".join(newStudentIDArray):
            newStudentIDArray = np.concatenate((newStudentIDArray, np.array([studentIDArray[i]])))

        else:
            # If the studentID is already added, it means that it is a duplicant, so the student is equal to
            # this studentIDArray[i] needs to be deleted from data, and this studentIDArray[i] will not be added
            # to the updated data.
            print("StudentID {} was deleted since it is a duplicant.".format(studentIDArray[i]))

            # Add this duplicant to an array (to delete)
            listOfOtherDuplicants.append(i)

            # Find position of the duplicant in the newStudentIDArray that needs to be deleted from the data
            otherDuplicantPos = np.where(newStudentIDArray == studentIDArray[i])
            listOfOtherDuplicants.append(otherDuplicantPos[0][0]) # to delete
    
    # Now, delete the duplicants from the data
    loadedDataArray = np.delete(loadedDataArray, listOfOtherDuplicants, axis=0)
    
    # Format data to show
    titles = list(loadedData)
    titles = titles[::]
    loadedDataFormatted = pd.DataFrame(loadedDataArray) 
    loadedDataFormatted.columns = titles

    # Print the updated data after removing student duplicants
    print("Here is the updated version of the data after checking for duplicant students: ")
    print(loadedDataFormatted)
    print('')


    ##############################################################


    ## Check for grade numbers that doesn't exist on the 7-step grading scale ##

    # Array containing possible grades that a student should be able to recieve
    possibleGrades = np.array([-3,0,2,4,7,10,12])
    
    # np.array containing the grades for each student
    grades = loadedDataArray[:,2:]

    # Round the grade to an excisting grade value via roundGrade function if the grade is not on the 7-step grading scale
    for i in range(grades.shape[0]):
        for j in range(grades.shape[1]):
            if grades[i,j] not in possibleGrades:
                print("The grade {} has been rounded to {}. The grade was recieved by {}, {} in {}.".format(grades[i,j], roundGrade(np.array([grades[i,j]]))[0], loadedDataArray[i,0], loadedDataArray[i,1], loadedData.columns[j+2]))
                loadedDataArray[i,j+2] = roundGrade(np.array([grades[i,j]]))[0]
    
    # Format data to show
    titles = list(loadedData)
    titles = titles[::]
    loadedDataFormatted = pd.DataFrame(loadedDataArray) 
    loadedDataFormatted.columns = titles

    # Print the updated data after checking for errors in grades
    print("Here is the updated version of the data after checking for errors in grades: ")
    print(loadedDataFormatted)

    # Return the updated, checked data
    return loadedDataArray