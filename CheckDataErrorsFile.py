# Importing libraries
import numpy as np

# Import other files
from DataLoadFile import dataLoad

# Import function used for global variables
import globalVariablesFile as g

def checkErrors(loadedData):

    # Array containing studentID for each student
    studentIDArray = np.array(loadedData.StudentID)

    # Array containing possible grades that a student should be able to recieve
    possibleGrades = np.array([-3,0,2,4,7,10,12])

    print('Hello!')