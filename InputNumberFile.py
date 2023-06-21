def inputNumber(prompt: str) -> float:
# This function was created during the exercises in module 5.

    ''' INPUTNUMBER Prompts user to input a number
    
        Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
        number. Repeats until user inputs a valid number.
    
        Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    '''

    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            return 0
    
    return num
