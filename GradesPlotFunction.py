# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 08:16:18 2023

@author: migpi
"""
# Importing libraries
import numpy as np
import math
import matplotlib.pyplot as plt

# Import other files
from displayMenuFile import displayMenu
from FinalGradeFunction import computeFinalGrades

# Import function used for global variables
import globalVariablesFile as g

def gradesPerAssignment(loadedData,grades):
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    # List with titles from data
    grades = grades
    loadedData = loadedData
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
        x = np.concatenate((x,np.ones(len(data[1]))*i))
        i+=1
    # Creating mean values:
    i = 0
    meanValues = np.zeros(len(data))
    while i < len(data):
        meanValues[i] = np.mean(np.asarray(data[i],"int"))
        i+=1
    #while i < len(data):
        
    #Creating y axis:
    y = np.asarray(np.reshape(data, -1),dtype='float')
    #Randomization Algorithm
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
    plt.plot(x, y, "r*")
    plt.plot(a, meanValues,label="Mean")
    plt.title("Grades for each assignment")
    plt.yticks([-3,0,2,4,7,10,12])
    plt.xlabel("Assignments")
    plt.ylabel("Grades")
    plt.xticks(a, names)
    plt.legend()
    plt.grid()
    plt.show()

def finalGrades(loadedData,grades):
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
    # creating the bar plot (This has been inspired by a github discussion post)
    plt.bar(Grade, Amount, color ='green',
            width = 0.4)
    plt.xlabel("Grade on 7-step scale")
    plt.ylabel("Amount of individual grade")
    plt.title("Distribution of grades")
    plt.grid()
    plt.show()
    # Plot is now shown onscreen


def plotFunction(grades, loadedData):
    while True:
        menuItems = np.array(["1. Plot: Grades Per Assignment", "2. Plot: Final Grades Distribution", "3. Return to menu"])
        menuChoice = displayMenu("Please enter a number corresponding to your choice of plot", menuItems)

        if menuChoice == 1:
            print(" ")
            result = gradesPerAssignment(loadedData,grades)

            print(result)       

        elif menuChoice == 2:
            print(" ")
            result = finalGrades(loadedData,grades)
            print(result)
           
            
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
