import tkinter
from tkinter import *
from PIL import Image, ImageTk


#LABELS AND IMAGES
'''
Variables to keep the label maker from getting cluttered
'''
root = Tk()
varOne = StringVar()

#There are a lot of parameters you can put into a label, link on Final Project Google Doc
labelOne = Label(root, textvariable = varOne, relief = RAISED, font=("Helvetica", 16), fg = "Purple" )

#This sets the string variable to text
varOne.set("Sam")
'''
.pack() is an organizer for labels within the window, it fits them in neatly
'''
labelOne.pack()


image = Image.open("Flowers1.jpg") #This opens the image using the PIL Image library
photo = ImageTk.PhotoImage(image) #Uses a function in the Image library ImageTk to make it compatible with Tkinter


#There are a lot of parameters you can put into a label, link on Final Project Google Doc
labelTwo = Label(root, image = photo, relief = RAISED)

labelTwo.image = photo

'''
.pack() is an organizer for labels within the window, it fits them in neatly
'''
labelTwo.pack()


'''
mainloop() is like an infinite loop that runs the program until the user closes the window
'''



#BUTTONS http://effbot.org/tkinterbook/button.htm
def callback():
    print ("Click")

buttonOne = Button(root, activebackground = 'red', command = callback, text = "SAM")
buttonOne.pack(fill = BOTH, expand = 1)

mainloop()