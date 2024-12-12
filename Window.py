import os
import string
import random
os.environ["TCL_LIBRARY"] = r"C:\Users\hector.mcewen\AppData\Local\Programs\Python\python313\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\hector.mcewen\AppData\Local\Programs\Python\python313\tcl\tk8.6"
from tkinter import *
root = Tk()
PasswordLet = []
PasswordNum = []

root.title("password generator")

for i in range(1, 12):
    PasswordLet.extend(random.choice(string.ascii_letters))
    PasswordLet.insert(random.randint(0, len(PasswordLet)) ,random.randint(1,9))

def myClick():
    MyLabel = Label(root, text={*PasswordLet})
    MyLabel.pack()
MyButton = Button(root, text="Create Password", command=myClick)
MyButton.pack()
# MyLabel2 = Label(root, text="Hello")
# MyLabel2.grid(row=1,column=1)
root.mainloop()