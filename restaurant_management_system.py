import tkinter as tk
from tkinter import ttk,messagebox

class RestaurantOrderManagement:
    def __init__(self,root):
        self.root =  root
        self.root.title("Restaurant Management App")

        self.menu_items = {
            "DRINKS": 1,
            "FRIES": 2,
            "BURGER": 3,
            "PIZZA": 4,
            "BIRIYANI": 5
        }

        self.exchange_rate = 80

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        ttk.Label(frame,
                  text="Restaurant order Management",
                  font=("Arial",20,"bold")).grid(row=0,
                                                 columnspan=3,
                                                 padx=10,
                                                 pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label = ttk.Label(frame,text=f"{item}(${price}):",font=("Arial",12))

            label.grid(row=1,column=0,padx=10,pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(frame,
                  text="Currency:",
                  font=("Arial",12)).grid(row=len(self.menu_items) + 1,
                                          column=0,
                                          padx=10,
                                          pady=5)

        currency_dropdown = ttk.Combobox(frame,
                                         textvariable=self.currency_var,
                                         state="ReadOnly",
                                         width=18,
                                         values=("USD","BDT"))
        currency_dropdown.grid(row=len(self.menu_items) + 1,
                               column=1,
                               padx=10,
                               pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace('w',self.update_menu_prices)

        order_button = ttk.Button(frame,
                                  text="Place Order",
                                  command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2,
                          columnspan=3,
                          padx=10,
                          pady=10)
        
    def setup_background(self,root):
        bg_width,bg_height = 800,600
        canvas = tk.Canvas(root,width=bg_width,height=bg_height)
        canvas.pack()