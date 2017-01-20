from tkinter import *

root = Tk()

def evaluate(event):
    name = entryOne.get()
    print (name)
    label.configure(text = name)


label = Label(root)

entryOne = Entry(root)

label.grid()
entryOne.grid(row = 1)
mainloop()