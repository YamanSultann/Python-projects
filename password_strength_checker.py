import tkinter as tk

def check_password_strength():
    password = password_entry.get()
    strength = ""

    if len(password) == 0:
        strength = "Password cannot be empty"
    elif len(password) < 6:
        strength = "Weak (too short)"
    elif len(password) < 10:
        strength = "Moderate"
    else:
        strength = "Strong"

    result_label.config(text=f"Strength: {strength}")

app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("400x200")

password_label = tk.Label(app,text="Enter Password: ")
password_label.pack()

password_entry = tk.Entry(app,show="*")
password_entry.pack(pady=5)

check_button = tk.Button(app,text="Check Strength",command=check_password_strength)
check_button.pack()

result_label = tk.Label(app, text="",)
result_label.pack(pady=10)

app.mainloop()