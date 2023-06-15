### Group GAUSS? ### #TO-DO: insert real group number
### Group Elif File ###

'''
Requires minimum Python 3.9. Otherwise delete the type declaration on function parameters.
'''

# Importing libraries
import numpy as np
import math

# Import other files
from DataLoadFile import convertLoadedDataToGrades
from DataLoadFile import dataLoad
from displayMenuFile import displayMenu
from GradesPlotFunction import plotFunction
from CheckDataErrorsFile import checkErrors

# Import function used for global variables
import globalVariablesFile as g


### MAIN SCRIPT ###
# Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023

# Initializing global variables (from global variable function in globalVariablesFile)
g.init()

# Ask user to load data
print("Please enter a valid filename in .csv format.")
loadedData = dataLoad()
grades = convertLoadedDataToGrades(loadedData)

# While loop to show menu until the user press the quit button
while True:
    
    print('')
    print("Datafile: " + g.globalDataFile)
    print("Checked for errors?: " + g.globalCheckErrors)


    # Show menu
    menuItems = np.array(["1. Load new data", "2. Check for data errors", "3. Generate plots", "4. Display list of grades", "5. Quit"])
    menuChoice = displayMenu("Please enter one of the numbers corresponding to a menu", menuItems)

    # If the user choose to "Load new data"
    if menuChoice == 1:
        loadedData = dataLoad()
        grades = convertLoadedDataToGrades(loadedData)

    # If the user choose to "Check for data errors"
    elif menuChoice == 2:
        checkErrors(loadedData)

    # If the user choose to "Generate plots"
    elif menuChoice == 3: 
        print('choice3')
        #plotFunction()

    # If the user choose to "Display list of grades"
    elif menuChoice == 4:
        print('choice 4')

    # If the user choose to "Quit" 
    elif menuChoice == 5:
        print("Quit has been chosen. I hope you enjoyed experiencing our menu. :^)")
        break

    else:
        pass