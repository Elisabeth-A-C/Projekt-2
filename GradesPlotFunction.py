"""
The two first functions in this file is used to make the two plots that
the user can choose between, and these two functions are used in the last 
function that shows the menu for the plots.

Author: Filip Pisinger, s224072@dtu.dk, 2023

"""

# Importing libraries
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

# Import other files
from DisplayMenuFile import displayMenu
from FinalGradeFunction import computeFinalGrades

# Import function used for global variables
import GlobalVariablesFile as g


def gradesPerAssignment(loadedData: pd.DataFrame, grades: np.float64) -> None:
    # List with titles from data
    inp = grades.T
    inp = np.array(inp)
    names = list(loadedData)
    names = names[2::]
    #The grades of each asnp.array(inp)signment is split to be put on axis:
    data = inp
    #Creating x axis list corresponding to assignments:
    x = np.array([])
    i=0
    while i < len(data):
        x = np.concatenate((x,np.ones(len(data[0]))*i))
        i+=1
    # Creating mean values:
    i = 0
    meanValues = np.zeros(len(data))
    while i < len(data):
        meanValues[i] = np.mean(np.asarray(data[i],"int"))
        i+=1
        
    #Creating y axis:
    y = np.asarray(np.reshape(data, -1),dtype='float')

    #Randomization Algorithm to visualize individual grades of same value
    i=0
    while i < len(x):
        x[i] += np.random.uniform(-0.1, 0.1, 1)[0]
        y[i] += np.random.uniform(-0.1, 0.1, 1)[0]
        i+=1

    a = list(range(0,len(meanValues)))

    #Relabelling of the x axis:
    xAxisTicks=([])
    i=0
    while i<len(names):
        xAxisTicks += [names[i]] * len(names)
        i+=1
    # plotting
    plt.plot(x, y, "ro", markersize = 2)
    plt.plot(a, meanValues)
    plt.title("Grades for each assignment")
    plt.yticks([-3,0,2,4,7,10,12])
    plt.xlabel("Assignments")
    plt.ylabel("Grades")
    plt.xticks(a, names)
    plt.legend(["Grades" , "Mean"]) # obs: the line for mean cannot be seen in data file 'moredata.csv' since there's only 1 assignment and therfore mean cannot be computed
    plt.grid()
    plt.show()

def finalGrades(loadedData: pd.DataFrame, grades: np.float64) -> None:
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    #The NxM matrix is made into a single vector of grades, to manage counting:
    inp = computeFinalGrades(grades)
    inp = inp.astype('int')
    inp = list(inp.astype('str'))
    #Counting amount of grades
    data = np.array([inp.count("-3"),inp.count("0"),inp.count("2"),inp.count("4"),inp.count("7"),inp.count("10"),inp.count("12")])
    #Input Data in plot:
    inp = {'-3':data[0], '00':data[1], '02':data[2], '4':data[3],'7':data[4],'10':data[5],'12':data[6]}
    Grade = list(inp.keys())
    Amount = list(inp.values())
    fig = plt.figure(figsize = (10, 5))
    # creating the bar plot:
    plt.bar(Grade, Amount, color ='green',
            width = 0.4)
    plt.xlabel("Grade on 7-step scale")
    plt.ylabel("Number of students whom have received grade")
    plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(1)) # to only show integers on y-axis
    plt.title("Distribution of grades")
    plt.grid(axis="y")
    plt.show()
    # Plot is now shown onscreen


# We have choosen to give the gradePlot function the inputs checkedDataArray and loadedData wherefrom we compute 'grades'
# ~ since we will need the columns from the .csv file for the plots, and grades is only the grades and in a np.array.
def gradesPlot(checkedDataArray: np.float64, loadedData: pd.DataFrame) -> None:
    # We have chosen to make the plot function dependent on input, so that the user of the interface,
    # ~ may themselves choose which plot to show onscreen.
    # Since the latest plot will always be in the way of the prior plotted.

    # Compute grades from checkedDataArray (in case the user has clicked on "Check for data errors" button)
    grades = checkedDataArray[:,2:]

    while True:

        menuItems = np.array(["1. Plot: Grades Per Assignment", "2. Final Grades Distribution", "3. Return to menu"])
        menuChoice = displayMenu("Please enter a number corresponding to your choice of plot", menuItems)

        if menuChoice == 1:
            # Plotes the grades per assignment:
            gradesPerAssignment(loadedData,grades)    

        elif menuChoice == 2:
            # Plots the final grades:
            finalGrades(loadedData,grades)
        
        elif menuChoice == 3:
            # Go back to menu
            print(" ")
            print("Returning to Menu")
            print(" ")
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