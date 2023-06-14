# Importing libraries
import numpy as np
import math
import matplotlib.pyplot as plt

# Import other files
from inputNumberFile import inputNumber

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
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber(prompt + ": ") # obs: there is a bug in Visual Studio Code where it sometimes only loads the menu after some buttom has been pressed but this does not occur in Jupyter Notebook
        if not(np.any(choice == np.arange(len(options))+1)):
            print(prompt + ".")

    return choice
