### Group GAUSS? ### #TO-DO: insert real group number
### Group Elif File ###

'''
Requires minimum Python 3.9. Otherwise delete the type declaration on function parameters.
'''

# Importing libraries
import numpy as np
import math

# Import other files
from DataLoadFile import dataLoad
from displayMenuFile import displayMenu


### MAIN SCRIPT ###
# Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023

# Ask user to load data
print("Please enter a valid filename in .csv format.")
loadedData = dataLoad()

# While loop to show menu until the user press the quit button
while True:
    # Show menu
    menuItems = np.array(["1. Load new data", "2. Check for data errors", "3. Generate plots", "4. Display list of grades", "5. Quit"])
    menuChoice = displayMenu("Please enter one of the numbers corresponding to a menu", menuItems)

    # If the user choose to "Load data"
    if menuChoice == 1:
        print('choice 1')

    # If the user choose to "Check for data errors"
    elif menuChoice == 2:
        print('choice 2')

    # If the user choose to "Generate plots"
    elif menuChoice == 3: 
        print('choice 3')

    # If the user choose to "Display list of grades"
    elif menuChoice == 4:
        print('choice 4')

    # If the user choose to "Quit" 
    elif menuChoice == 5:
        print("Quit has been chosen. I hope you enjoyed experiencing our menu. :^)")
        break

    else:
        pass