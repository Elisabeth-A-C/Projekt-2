'''
The first function in this file loads the data in a pd.DataFrame format,
and the second file converts the data into an np.array format that only 
contains the grades for the assignments.

'''

# Importing libraries
import numpy as np
import pandas as pd

# Import function used for global variables
import GlobalVariablesFile as g


def dataLoad() -> pd.DataFrame:
    '''
    ### Function used to load data from a .csv file and display the loaded data.
    
    Parameters:
        This is a void function.
    
    Returns:
        - loadedData (pd.DataFrame): The data in pd.Dataframe format after it has been loaded from a .csv file

    Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023
    '''

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


def convertLoadedDataToGrades(loadedData: pd.DataFrame) -> np.float64:
    '''
    ### Function used to convert loaedData (.csv format) to grades (np.array format with just the grades for the assignments).
    
    Parameters:
        - loadedData (pd.DataFrame): The original data directly from the .csv file, in pd.Dataframe format
    
    Returns:
        - grades (np.float64): The data in np.array format, with just the grades for the assignments
        
    Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023
    '''

    # Convert loadedData to grades
    grades = loadedData.iloc[:,2:]
    grades = np.array(grades)

    # Return loaded data
    return grades