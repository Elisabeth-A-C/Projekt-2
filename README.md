# Projekt-2

## Introduction
In this project, we have created a program where the user can upload a comma-separated .csv file containing data for student grades. 
The .csv file needs to be complete, and it needs to contain the following information:

    StudentID, Name, Assignment 1, Assignment 2, Assignment 3, etc.

Where the number of Assignments needs to be at least 1, and the number of students needs to be at least one. The user can choose to load new data in the main menu.

In the main menu, the user can also choose to check the data for data errors (student duplicates and grades that are not included in the 7-step grading scale), generate plots (showing final grades or grades per assignment), display the data including the calculated final grade, or to quit the program. At all times, the user can enter '5050' as input in a menu (e.g. main menu og plot menu) to quit the program, and the user will be asked one more time if wanting to quit the program.


## Code structure
The main script contains the main menu in the program. The program is run in a while-loop, and the program is quit by breaking the while-loop. 
The code also contains several other files with the functions that are called in the main script and in other functions, and it contains several datafiles 
that has been used for bug-testing in the program.
