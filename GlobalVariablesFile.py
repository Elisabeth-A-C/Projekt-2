def init():
    # Function made for initializing global variables, used to show update on loaded datafile name and if the data has been checked for errors
    
    # Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023

    global globalDataFile
    globalDataFile = "None" # global variable made to show the name of the loaded datafile

    global globalCheckErrors
    globalCheckErrors = "No" # global variable made to show if the data has been checked for errors

    global pleaseQuitProgram
    pleaseQuitProgram = False # global variable made to be able to quit the program at all times
