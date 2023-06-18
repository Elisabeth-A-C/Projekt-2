# Projekt-2

## Introduction
In this project, we have created a program where the user can upload a comma-separated .csv file containing data for student grades. 
The .csv file needs to be complete, and it needs to contain the following information:

    StudentID, Name, Assignment 1, Assignment 2, Assignment 3, etc.

Where the number of Assignments needs to be at least 1, and the number of students needs to be at least one. The user can choose to load new data in the main menu.

In the main menu, the user can also choose to check the data for data errors (student duplicates and grades that are not included in the 7-step grading scale), generate plots (showing final grades or grades per assignment), display the data including the calculated final grade, or to quit the program. At all times, the user can enter '5050' as input in a menu (e.g. main menu and plot menu) to quit the program, and the user will be asked one more time if wanting to quit the program.


## Code structure
The main script contains the main menu in the program. The program is run in a while loop, and the program is quit by breaking the while loop. 
The code also contains several other files with the functions that are called in the main script and in other functions, and it contains several data files 
that has been used for bug testing in the program.


## Grade rounding function
Filip writes...


## Final grade function
The final grade function computes the final grade for each student from the assignment grades. If there's only one assignment for each student, this must be the final grade. If a student has received -3 in one or more of the assignments, the student must receive the final grade -3. Otherwise, the final grade is calculated from the average of all assignments when the lowest grade is removed. The grade is then rounded to a valid grade on the 7-step grading scale, using the roundGrade function.


## Grades plot function
Filip writes...


## Main script
The main script consists of the main menu in the program. Before the user gets to the menu, the user must enter a valid .csv data file. The main menu is run in a while loop, and the program stops when the while loop is broken. 
In the main menu, the user can choose to:
        
    ### 1. "Load new data". This is done in the same way as when the data was loaded at the beginning of the program. 
        
    2. "Check for data errors". This is done using the checkErrors function. 
    Duplicate students are removed, and grades not on the 7-step grading scale are rounded to a valid grade.
        
    3. "Generate plots". This is done using functions from the GradesPlotFunction file.
        
    4. "Display list of grades". This is done using the displayListOfGrades function. 
    The data is shown, now including the final grade for each student, calculated using the computeFinalGrades function. 
        
    5. "Quit". This is done by breaking the while loop that the main menu runs in. 


## Global variables
To make it possible to use global variables in Python, the global variables have been defined in the globalVariablesFile which contains the init function that initializes the global variables. This function is called at the beginning of the main script so that the global variables are initialized here. The global variables can then be called when writing 'import globalVariablesFile as g' at the beginning of a file, and by calling the global variable with 'g.' in front of the global variable name.
