import random

def guess(x):
    toGuess = random.randint(1, x)
    myGuess = 0
    while myGuess is not toGuess:
        myGuess = int(input(f'give number between 1 and {x} : '))
        if myGuess < toGuess : print("too low")
        elif myGuess > toGuess: print("too high")
        else: print(str(toGuess) + " is the number")
#guess(10)
def computerGuess(x):
    toGuess = random.randint(1, x)
    myGuess = 0
    low = 1
    high = x
    while myGuess is not toGuess:
        myGuess = random.randint(low, high)
        print(myGuess)
        if myGuess < toGuess: low = myGuess
        elif myGuess > toGuess: high = myGuess
        else: print("hey")
#computerGuess(790)

computerGuess(10)