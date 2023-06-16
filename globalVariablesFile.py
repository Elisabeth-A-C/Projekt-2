def init():
    # Function made for initializing global variables, used to show update on loaded datafile name and filters active
    
    # Author: Elisabeth Astrup Christensen, s224063@dtu.dk, 2023

    global globalDataFile
    globalDataFile = "None" # global variable

    global globalCheckErrors
    globalCheckErrors = "No" # global variable

    global pleaseQuitProgram
    pleaseQuitProgram = False # global variable made to be able to quit the program at all times