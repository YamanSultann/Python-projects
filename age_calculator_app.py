import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        dob = datetime(year, month, day)
        today = datetime.now()
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day

        if age_days < 0:
            age_months -= 1
            age_days += 30

        if age_months < 0:
            age_years -= 1
            age_months += 12

        result_label.config(text=f"Your Age: {age_years} years, {age_months} months, and {age_days} days.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid date.")


app = tk.Tk()
app.title("Age Calculator")
app.geometry("400x300")

day_label = tk.Label(app, text="Day:", font=("Arial", 12))
day_label.pack(pady=5)
day_entry = tk.Entry(app, font=("Arial", 12))
day_entry.pack(pady=5)

month_label = tk.Label(app, text="Month:", font=("Arial", 12))
month_label.pack(pady=5)
month_entry = tk.Entry(app, font=("Arial", 12))
month_entry.pack(pady=5)

year_label = tk.Label(app, text="Year:", font=("Arial", 12))
year_label.pack(pady=5)
year_entry = tk.Entry(app, font=("Arial", 12))
year_entry.pack(pady=5)

calculate_button = tk.Button(app, text="Calculate Age", font=("Arial", 12), command=calculate_age)
calculate_button.pack(pady=15)

result_label = tk.Label(app, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

app.mainloop()