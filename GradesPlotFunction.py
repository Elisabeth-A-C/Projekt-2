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

def gradesPerAssignment(grades):
    inp = grades
    names = inp[0]
    #The grades of each assignment is split to be put on axis:
    data = inp[1::]
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
    plt.ylabel("Grades")
    plt.xticks(a, names)
    plt.legend()
    plt.grid()
    plt.show


def finalGrades(grades):
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    #The NxM matrix is made into a single vector of grades, to manage counting:
    inp = grades[1::]
    inp = np.reshape(inp, -1)
    inp = list(inp.astype('str'))
    #Counting amount of grades
    data = np.array([inp.count("-3"),inp.count("0"),inp.count("2"),inp.count("4"),inp.count("7"),inp.count("10"),inp.count("12")])
    print(data)
    #Input Data in plot:
    inp = {'-3':data[0], '00':data[1], '02':data[2], '4':data[3],'7':data[4],'10':data[5],'12':data[6]}
    Grade = list(inp.keys())
    Amount = list(inp.values())
    fig = plt.figure(figsize = (10, 5))
    # creating the bar plot (This has been inspired by a github discussion post)
    plt.bar(Grade, Amount, color ='green',
            width = 0.4)
    plt.xlabel("Grade on 7-step scale")
    plt.ylabel("Amount of individual grade")
    plt.title("Distribution of grades")
    plt.show()
    # Plot is now shown onscreen



def plotFunction(loadedData):
    while True:
        menuItems = np.array(["1. Plot: Grades Per Assignment", "2. Final Grades Distribution", "3. Return to menu"])
        menuChoice = displayMenu("Please enter a number corresponding to your choice of plot", menuItems)

        if menuChoice == 1:
            print(" ")
            result = gradesPerAssignment(loadedData)
            #Prints
            print(result)       

        elif menuChoice == 2:
            # The user needs to choose filter on range of growth rate
            print(" ")
            result = finalGrades(loadedData)
            #print("The distribution of bacteria by numbers is: {:f}".format(result))
            print(result)
        
        elif menuChoice == 3:
            # Go back to menu
            print(" ")
            print("Returning to Menu")
            print(" ")
            break
