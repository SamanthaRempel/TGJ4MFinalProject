import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageFilter

clicked = True
root = Tk()

root.geometry('500x400+30+30')

photoShopImage = Image.open("Flowers1.jpg")

pic = Image.open("Flowers1.jpg")  # This opens the image using the PIL Image library
photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter

label = Label(root, image=photo)
label.image = photo
label.place(x=100, y=100)
label.pack(side=RIGHT)


def blackAndWhite():
    '''
    Makes the image black and white
    :return: No return
    '''
    photoShopImage = Image.open("Flowers1.jpg")
    label.pack_forget()
    photoShopImage = photoShopImage.convert("L")
    photoSIE = ImageTk.PhotoImage(photoShopImage)
    label.configure(image=photoSIE)
    label.image = photoSIE
    label.place(x=100, y=100)
    label.pack(side=RIGHT)

def colour():
    '''
    Reverts the image back to colour
    :return: No return
    '''
    photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter
    label.configure(image=photo)
    label.image = photo
    label.place(x=100, y=100)
    label.pack(side=RIGHT)

def blur():
    '''
    Reverts the image back to colour
    :return: No return
    '''
    photoShopImage = Image.open("Flowers1.jpg")
    label.pack_forget()
    photoShopImage = photoShopImage.ImageFilter.GausianBlur(radius = 2)
    photoSIE = ImageTk.PhotoImage(photoShopImage)
    label.configure(image=photoSIE)
    label.image = photoSIE
    label.place(x=100, y=100)
    label.pack(side=RIGHT)

# Button for black and white
buttonBW = Button(root, activebackground='red', command=blackAndWhite, text="Black and White")
buttonBW.pack(side=LEFT)

# Button for Colour
buttonCLR = Button(root, activebackground='red', command=colour, text="Colour")
buttonCLR.pack(side=LEFT)

#Button for Blur
buttonBLR = Button(root, command = blur, text = "Blur")
buttonBLR.pack(side = LEFT)

mainloop()
