'''
Program header goes here
'''

import tkinter
from tkinter import *
from PIL import Image, ImageTk
countBW = 0
root = Tk()
def blackAndWhite(countBW):
    label.pack_forget()
    if countBW%2 == 0:

        photoShopImageEdit = photoShopImage.convert("L")
        photo = ImageTk.PhotoImage(photoShopImageEdit)


    else:
        photo = ImageTk.PhotoImage(pic)

    label.configure(image=photo)
    label.image = photo
    label.pack()
    countBW += 1
# BUTTONS http://effbot.org/tkinterbook/button.htm

photoShopImage = Image.open("Flowers1.jpg")

pic = Image.open("Flowers1.jpg")  # This opens the image using the PIL Image library
photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter

label = Label(root, image = photo)
label.image = photo
label.place(x = 50, y = 50)
label.pack()



buttonOne = Button(root, activebackground='red', command=blackAndWhite(countBW), text="Black and White")
buttonOne.pack(fill=BOTH, expand=1)



mainloop()