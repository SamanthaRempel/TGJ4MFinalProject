import tkinter
from tkinter import *
from PIL import Image, ImageTk
clicked = True
root = Tk()

photoShopImage = Image.open("Flowers1.jpg")

pic = Image.open("Flowers1.jpg")  # This opens the image using the PIL Image library
photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter

label = Label(root, image = photo)
label.image = photo
label.place(x = 100, y = 100)
label.pack()

def blackAndWhite():
    photoShopImage = Image.open("Flowers1.jpg")
    label.pack_forget()
    photoShopImageEdit = photoShopImage.convert("L")
    photoSIE = ImageTk.PhotoImage(photoShopImageEdit)
    label.configure(image=photoSIE)
    label.image = photoSIE
    label.place(x=100, y=100)
    label.pack()


def colour():
    photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter
    label.configure(image=photo)
    label.image = photo
    label.place(x=100, y=100)
    label.pack()
# BUTTONS http://effbot.org/tkinterbook/button.htm

buttonOne = Button(root, activebackground = 'red', command = blackAndWhite, text = "Black and White")
buttonOne.place(x = 20, y = 40)
buttonOne.pack(padx = 5, pady = 10, side = LEFT)
buttonTwo = Button(root, activebackground = 'red', command = colour, text = "Colour")
buttonTwo.place(x = 20, y = 20)
buttonTwo.pack(padx = 5, pady = 20, side = LEFT)

mainloop()
