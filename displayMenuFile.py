# Importing libraries
import numpy as np
import math

# Import other files
from inputNumberFile import inputNumber

# Import function used for global variables
import globalVariablesFile as g

def displayMenu(prompt: str, options: str) -> float:
# This function was created during the exercises in module 5.

    ''' DISPLAYMENU Displays a menu of options, ask the user to choose an item
        and returns the number of the menu item chosen.
    
        Usage: choice = displayMenu(prompt, options)
    
        Input options: Promt and Menu options (array of strings)
        Input prompt: Prompt text (string)
        Output choice: Chosen option (float)

        Inspired by: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
     '''
    
    print('')
    print(prompt + '.')

    # Display menu options
    for i in range(len(options)):
        print("{:s}".format(options[i]))

    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == (np.arange(len(options))+1)) or (choice == 5050)):
        choice = inputNumber(prompt + ": ") 

        # Quit program option if user enters 5050
        if choice == 5050: # 5050 since that is all numbers from 1 to 100, summed
            g.pleaseQuitProgram = True
            break
        elif not(np.any(choice == np.arange(len(options))+1)):
            print(prompt + ".")

    return choice
