import tkinter as tk

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        
        simple_interest = (principal * time * rate) / 100

        compound_interest = principal * ((1 + (rate / 100)) ** time) - principal
        
        si_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        ci_label.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")

app = tk.Tk()
app.title("Interest Calculator")
app.geometry("400x400")

principal_label = tk.Label(app, text="Principal Amount:", font=("Arial", 14))
principal_label.pack(pady=5)
principal_entry = tk.Entry(app, font=("Arial", 14))
principal_entry.pack(pady=5)

time_label = tk.Label(app, text="Time Period (in years):", font=("Arial", 14))
time_label.pack(pady=5)
time_entry = tk.Entry(app, font=("Arial", 14))
time_entry.pack(pady=5)

rate_label = tk.Label(app, text="Rate of Interest (in %):", font=("Arial", 14))
rate_label.pack(pady=5)
rate_entry = tk.Entry(app, font=("Arial", 14))
rate_entry.pack(pady=5)

calculate_button = tk.Button(app, text="Calculate", font=("Arial", 12), command=calculate_interest)
calculate_button.pack(pady=15)

si_label = tk.Label(app, text="", font=("Arial", 14), fg="blue")
si_label.pack(pady=5)

ci_label = tk.Label(app, text="", font=("Arial", 14), fg="blue")
ci_label.pack(pady=5)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

app.mainloop()
        