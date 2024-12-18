import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get inputs from entry fields
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate the product
        product = num1 * num2
        
        # Display the result
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Product Calculator")
app.geometry("300x200")

# Create and place widgets
label1 = tk.Label(app, text="Enter first number:")
label1.pack(pady=5)

entry1 = tk.Entry(app)
entry1.pack(pady=5)

label2 = tk.Label(app, text="Enter second number:")
label2.pack(pady=5)

entry2 = tk.Entry(app)
entry2.pack(pady=5)

calculate_button = tk.Button(app, text="Calculate Product", command=calculate_product)
calculate_button.pack(pady=10)

result_label = tk.Label(app, text="Product: ")
result_label.pack(pady=5)

# Run the application
app.mainloop()