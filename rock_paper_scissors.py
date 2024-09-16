import random

user_action = input("Please enter yout choice(rock, paper or scissor): ")
possible_actions = ["rock","paper","scissor"]
computer_action = random.choice(possible_actions)
print("You chose",user_action,"and the computer chose",computer_action)
if user_action == computer_action:
    print("It's a TIE, no one wins")
elif user_action == "rock":
    if computer_action == "paper":
        