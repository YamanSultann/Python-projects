import random
playing = True
number = str(random.randint(1,10))

print("I will generate a number from 1 to 10 and you have to guess the it!")
print("The game ends when you get 1 correct")
while playing:
    guess = input("Enter your guess here: ")
    if guess == number:
        print("CONGRATULATIONS YOU WON!")
        break
    else:
        print("Try again, your guess was not quite right")
