import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    user_choice_label.config(text=f"Your choice: {choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)

app = tk.Tk()
app.title("Rock-Paper-Scissors Game")
app.geometry("400x300")

instruction_label = tk.Label(app, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
instruction_label.pack(pady=10)

rock_button = tk.Button(app, text="Rock", font=("Arial", 12), command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(app, text="Paper", font=("Arial", 12), command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(app, text="Scissors", font=("Arial", 12), command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

user_choice_label = tk.Label(app, text="Your choice: ", font=("Arial", 12))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(app, text="Computer's choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

app.mainloop()