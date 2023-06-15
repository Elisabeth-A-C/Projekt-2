# Importing libraries
import numpy as np
import pandas as pd

# Import function used for global variables
import globalVariablesFile as g

def dataLoad():
    # Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023

    # Load data if it exists
    found = False
    while not found:
        try:
            filename = input("Enter filename: ")
            loadedData = pd.read_csv(filename)
            found = True
            print("Data has been succesfully loaded.")

            # Setting global variable used to show filename
            g.globalDataFile = filename

        except: 
            print("Couldn't load the file. Please enter a valid filename.")
            continue

    
    # Display loaded data
    print('Here is the data loaded: ')
    print('')
    print(loadedData)
    print('')

    # Display number of students
    numberOfStudents = len(loadedData.StudentID)
    print("The number of students is: {}".format(numberOfStudents))
    print('')

    # Display number of assignments
    numberOfAssignments = len(loadedData.iloc[0,2:])
    print("The number of assignments is: {}".format(numberOfAssignments))
    print('')

    return loadedData


def convertLoadedDataToGrades():
    # Convert loadedData to grades
    loadedData = dataLoad()
    grades = loadedData.iloc[:,2:]
    grades = np.array(grades)

    # Return loaded data
    return grades