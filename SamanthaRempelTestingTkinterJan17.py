import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

photoShopImage = Image.open("Flowers1.jpg")

pic = Image.open("Flowers1.jpg")  # This opens the image using the PIL Image library
photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter

label = Label(root, image = photo)
label.image = photo
label.pack()

# BUTTONS http://effbot.org/tkinterbook/button.htm
def blackAndWhite():
    photoShopImageEdit = photoShopImage.convert("L")
    photo = ImageTk.PhotoImage(photoShopImageEdit)
    label = Label(root, image = photo)
    label.image = photo
    label.pack()

buttonOne = Button(root, activebackground='red', command=blackAndWhite, text="SAM")
buttonOne.pack(fill=BOTH, expand=1)

mainloop()