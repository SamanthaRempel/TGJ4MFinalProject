import tkinter
from tkinter import *
from PIL import Image, ImageTk
countBW = 0
root = Tk()

photoShopImage = Image.open("Flowers1.jpg")

pic = Image.open("Flowers1.jpg")  # This opens the image using the PIL Image library
photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter

label = Label(root, image = photo)
label.image = photo
label.place(x = 100, y = 100)
label.pack()

def blackAndWhite():
    label.pack_forget()
    if countBW % 2 == 0:
        photoShopImageEdit = photoShopImage.convert("L")
        photo = ImageTk.PhotoImage(photoShopImageEdit)
        label.configure(image=photo)
        label.image = photo
        label.place(x=100, y=100)
        label.pack()
    else:
        photo = ImageTk.PhotoImage(pic)
        label.image = photo
        label.place(x=100, y=100)
        label.pack()

# BUTTONS http://effbot.org/tkinterbook/button.htm

buttonOne = Button(root, activebackground='red', command=blackAndWhite, text="Black and White")

buttonOne.place(x = 500, y = 500)
buttonOne.pack(fill=BOTH, expand=1)

mainloop()
