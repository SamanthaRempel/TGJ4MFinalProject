from tkinter import *
from PIL import Image

root = Tk()  # Master window
name = ""
if name == "":
    def evaluate(event):
        '''

        :param event: This just says that the enter key has been pressed
        :return: No return
        '''
        name = entryOne.get()  # gets whatever data was entered into the text box
        print(name)
        label.configure(text=name)  # reconfigures the label to read the text entered in the text box


    label = Label(root)  # makes a blank label in the screen

    entryOne = Entry(root)  # Makes an empty text box for user entry
    entryOne.bind("<Return>", evaluate)  # This stores the information that was put into the text box

    # Places the label and entry box
    label.grid()
    entryOne.grid(row=1)

pic = Image.open(name)  # This opens the image using the PIL, it doesn't make the image usable in Tkinter
mainloop()
