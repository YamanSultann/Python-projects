import random

user_action = input("Please enter yout choice(rock, paper or scissor): ")
possible_actions = ["rock","paper","scissor"]
computer_action = random.choice(possible_actions)
print("You chose",user_action,"and the computer chose",computer_action)
if user_action == computer_action:
    print("It's a TIE, no one wins")
elif user_action == "rock":
    if computer_action == "paper":
        print("Paper beats rock, you LOSE")
    elif computer_action == "scissor":
        print("Rock beats scissor, you WIN")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper beats rock, you WIN")
    elif computer_action == "scissor":
        print("Scissor beats paper, you LOSE")
elif user_action == "scissor":
    if computer_action == "rock":
        print("Rock beats scissor, you LOSE")
    elif computer_action == "paper":
        print("Scissor beats paper, you WIN")