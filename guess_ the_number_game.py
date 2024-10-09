import random
import time

number = random.randint(1,100)

def intro():
    print("May I ask you for your name?")

    global name
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    if (number % 2 == 0):
        x = 'even'
    else:
        x = 'odd'
    
    print("This is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead. Guess!")