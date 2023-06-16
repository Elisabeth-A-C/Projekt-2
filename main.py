### Group GAUSS? ### #TO-DO: insert real group number
### Group Elif File ###

'''
Requires minimum Python 3.9. Otherwise delete the type declaration on function parameters.
'''

# Importing libraries
import numpy as np
import math

#Setting directory to current file directory
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Import other files
from DataLoadFile import convertLoadedDataToGrades
from DataLoadFile import dataLoad
from displayMenuFile import displayMenu
from GradesPlotFunction import plotFunction
from CheckDataErrorsFile import checkErrors
from DisplayListOfGradesFile import displayListOfGrades

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
    print("At all times you can enter '5050' in a menu to quit the program.")
    print("Datafile: " + g.globalDataFile)
    print("Checked for errors?: " + g.globalCheckErrors)


    # Show menu
    menuItems = np.array(["1. Load new data", "2. Check for data errors", "3. Generate plots", "4. Display list of grades", "5. Quit"])
    menuChoice = displayMenu("Please enter one of the numbers corresponding to a menu", menuItems)

    # If the user choose to "Load new data"
    if menuChoice == 1:
        loadedData = dataLoad()
        grades = convertLoadedDataToGrades(loadedData)
        g.globalCheckErrors = "No"

    # If the user choose to "Check for data errors"
    elif menuChoice == 2:
        checkedDataArray = checkErrors(loadedData)
        g.globalCheckErrors = "Yes"

    # If the user choose to "Generate plots"
    elif menuChoice == 3: 
        plotFunction(grades, loadedData) # TO-DO: insert updated data from checkErrors
        if g.pleaseQuitProgram == True:
            break

    # If the user choose to "Display list of grades"
    elif menuChoice == 4:
        if g.globalCheckErrors == "No":
            checkedDataArray = np.array(loadedData)
        elif g.globalCheckErrors == "Yes":
            pass
        displayListOfGrades(checkedDataArray, loadedData)

    # If the user choose to "Quit" 
    elif menuChoice == 5:
        print("Quit has been chosen. I hope you enjoyed experiencing our menu. :^)")
        break

    elif g.pleaseQuitProgram == True:
        menuItems = np.array(["1. Yes, quit the program.", "2. No, please go back to the previous menu."])
        menuChoice = displayMenu("Are you sure you want to quit the program?", menuItems)

        if menuChoice == 1:
            print("You have quit the program. I hope you enjoyed experiencing our menu. :^)")
            break
        if menuChoice == 2:
            g.pleaseQuitProgram = False
            continue

    else:
        pass