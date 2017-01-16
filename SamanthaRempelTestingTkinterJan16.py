import tkinter
from tkinter import *
from PIL import Image, ImageTk

photoShopImage = Image.open("Flowers1.jpg")

# LABELS AND IMAGES
'''
Variables to keep the label maker from getting cluttered
'''
root = Tk()
varOne = StringVar()

# There are a lot of parameters you can put into a label, link on Final Project Google Doc
labelOne = Label(root, textvariable=varOne, relief=RAISED, font=("Helvetica", 16), fg="Purple")

# This sets the string variable to text
varOne.set("Sam")

'''
.pack() is an organizer for labels within the window, it fits them in neatly
'''
labelOne.pack()


image = Image.open("Flowers1.jpg")  # This opens the image using the PIL Image library
photo = ImageTk.PhotoImage(image)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter

image2 = Image.open("Flowers2.jpg")
photo2 = ImageTk.PhotoImage(image2)

# There are a lot of parameters you can put into a label, link on Final Project Google Doc

labelTwo = Label(root, image=photo, relief=RAISED)
labelTwo.image = photo

'''
.pack() is an organizer for labels within the window, it fits them in neatly
'''
labelTwo.pack()

# BUTTONS http://effbot.org/tkinterbook/button.htm
def blackAndWhite():
    labelTwo.pack_forget()
    photoShopImageEdit = photoShopImage.convert("L")
    photo2 = ImageTk.PhotoImage(
    photoShopImageEdit)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter
    labelTwo.image = photo2
    labelTwo.pack()
    mainloop()


buttonOne = Button(root, activebackground='red', command=blackAndWhite, text="SAM")
buttonOne.pack(fill=BOTH, expand=1)


'''
mainloop() is like an infinite loop that runs the program until the user closes the window
'''
mainloop()
