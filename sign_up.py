from tkinter import *

root = Tk()
root.title('Sign up')
root.geometry('420x300')

lbl1 = Label(text="Full Name",bg="#3895D3",fg='white')
lbl2 = Label(text="Email",bg="#3985D3",fg='white')
lbl3 = Label(text="Password",bg="#3985D3",fg='white')

name_entry = Entry()
email_entry = Entry()
pass_entry = Entry(show="*")

def display():
    name = name_entry.get()
    greet = "Hey "+name
    message = "\nCongratulation of successfuly creating your account!"
    text_box.insert(END,greet)
    text_box.insert(END,message)

text_box = Text(bg="#BEBEBE",fg='black')

btn = Button(text = "Create account",command=display)

lbl1.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
pass_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()