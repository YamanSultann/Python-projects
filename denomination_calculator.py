from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x400")
root.title("Denomination Calculator")
root.configure(bg="light blue")

upload = Image.open("app_img.png")
upload = upload.resize(300 , 300)
image = ImageTk.PhotoImage(upload)
label = Label(root , image=image , bg="light blue")
label.place(x=180 , y=20)

label1 = Label(root , text = "Hey User! Welcome to Denomination Counter App." , bg = "light blue")
label1.place(relx=0.5 , y=340 , anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert" , "Do you want to calculate the denomination count?")
    if MsgBox == "Ok":
        topwin()

def topwin():
    top = Tk()
    top.geometry("650x400")
    top.title("Denomination Calculator")
    top.configure(bg="light blue")

    label2 = Label(top,text="Enter total amount")
    entry = Entry(top)
    label3 = Label(top,text="Here are the number of notes for each denomination",bg="light blue")
    l1 = Label(top,text="1000",bg="light grey")
    l2 = Label(top,text="100",bg="light grey")
    l3 = Label(top,text="10",bg="light grey")
    l4 = Label(top,text="1",bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note1000 = amount // 1000
            amount %= 1000
            note100 = amount // 100
            amount %= 100
            note10 = amount // 10
            amount %= 10
            note1 = amount // 1
            amount %= 1

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)

            t1.insert(END,str(note1000))
            t2.insert(END,str(note100))
            t3.insert(END,str(note10))
            t4.insert(END,str(note1))
        except ValueError:
            messagebox.showerror("Error","Please enter a valid amount")

    btn = Button(top,text="Calculate",cammond=calculate,bg="brown",fg="white")
    