from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("200x180")

def msg():
    messagebox.showwarning("Alert","Stop, virus found")

btn = Button(window,text="Scan for virus",command=msg)
btn.place(x=40,y=80)

window.mainloop()