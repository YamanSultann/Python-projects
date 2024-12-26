import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry.get())

        cm = inches * 2.54

        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

app = tk.Tk()
app.title("Inches to Centimeters Converter")
app.geometry("400x200")

instruction_label = tk.Label(app, text="Enter length in inches: ")
instruction_label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=5)

convert_button = tk.Button(app, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

result_label = tk.Label(app, text="", fg="blue")
result_label.pack(pady=10)

app.mainloop()