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

def checkErrors(loadedData):
    # Author: Elisabeth Astrup Christensen

    ## First check if the studentID is a duplicant, and delete the duplicants ##

    # loadedData as an np.array
    loadedDataArray = np.array(loadedData)

    # Array containing studentID for each student
    studentIDArray = np.array(loadedData.StudentID)

    # Remove duplicates from studentIDArray
    newStudentIDArray = np.array([])
    listOfOtherDuplicants = list() # to delete

    print('')

    for i in range(np.size(studentIDArray)):
        if studentIDArray[i] not in " ".join(newStudentIDArray):
            newStudentIDArray = np.concatenate((newStudentIDArray, np.array([studentIDArray[i]])))

        else:
            print("StudentID {} was deleted since it is a duplicant.".format(studentIDArray[i]))

            # Add this duplicant to an array
            listOfOtherDuplicants.append(i)

            # Where the first duplicant of the studentID is (delete this first duplicate too)
            otherDuplicantPos = np.where(newStudentIDArray == studentIDArray[i])
            listOfOtherDuplicants.append(otherDuplicantPos[0][0]) # to delete
    

    loadedDataArray = np.delete(loadedDataArray, listOfOtherDuplicants, axis=0)
    
    # Format data to show
    titles = list(loadedData)
    titles = titles[::]
    loadedDataFormatted = pd.DataFrame(loadedDataArray) 
    loadedDataFormatted.columns = titles

    print("Here is the updated version of the data after checking for duplicant students: ")
    print(loadedDataFormatted)
    print('')


    ##############################################################


    ## Check if there are any faulty grades for each studentID ##

    # Array containing possible grades that a student should be able to recieve
    possibleGrades = np.array([-3,0,2,4,7,10,12])
    
    # Array containing the grades for each student
    grades = loadedDataArray[:,2:]

    # Round the grade to an excisting grade value if the grade is faulty (via roundGrade function)
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

    print("Here is the updated version of the data after checking for errors in grades: ")
    print(loadedDataFormatted)

    return loadedDataArray # containing the checked data