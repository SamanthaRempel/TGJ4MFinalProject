import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

root = Tk()  # Master key stored in a variable so I can just use this to print to the screen

countR = 1

root.geometry('500x300+30+30')  # This sets the screen widthxheight+sidePadding+sidePadding

pic = Image.open("Flowers1.jpg")  # This opens the image using the PIL, it doesn't make the image usable in Tkinter
photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter

photoShopImage = Image.open("Flowers1.jpg")  # Opens the same iamge, but so that it is compatible with PIL
photoShopImageEdit = None  # Empty variable to test if any effects have been applied
widthI, heightI = photoShopImage.size

label = Label(root, image=photo, height = widthI, width = widthI )  # Creates a label with an image on it
label.image = photo  # Saves the image used in a seperate place so it doesn't get overwritten
label.pack(side=TOP)  # Send the image and centres it on the side indicated

def blackAndWhite():
    '''
    Makes the image black and white
    :return: No return
    '''
    global photoShopImageEdit, photoShopImage  # Imports global image varables to use to edit images
    if photoShopImageEdit == None:  # Only happens if B&W is the first effect, b/c it was blurring automatically
        photoShopImage = photoShopImage.convert("L")  # Converts the image to black and white
        photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
    else:  # If there has been effects applied to the original image
        photoShopImageEdit = photoShopImageEdit.convert("L")
        photoSIE = ImageTk.PhotoImage(photoShopImageEdit)
    label.configure(image=photoSIE, height = widthI, width = widthI )  # Takes the old label and changes the image, reconfigures it
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Puts the image at the top of the screen


def original():
    '''
    Reverts the image back to colour, with no effects
    :return: No return
    '''
    global photoShopImageEdit, photoShopImage  # Sends in the image variables being changed, b/c they need to reset
    photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter
    label.configure(image=photo, height = widthI, width = widthI )  # Reconfigures the label with the original image
    label.image = photo  # Saves new image so it doesn't get lost
    label.pack(side=TOP)  # Sends Image to the top
    photoShopImage = Image.open("Flowers1.jpg")  # Resets the photoshop image
    photoShopImageEdit = None  # MAkes it so the image hasn't been edited


def blur():
    '''
    Reverts the image back to colour
    :return: No return
    '''
    global photoShopImage  # Sends in the image variable being edited, only the B&W needs original image IDK why
    photoShopImage = photoShopImage.filter(ImageFilter.GaussianBlur(radius=1))  # Adds the blur effect, with radius 1
    photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
    label.configure(image=photoSIE, height = widthI, width = widthI )  # Reconfigures the image on the label
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Sends the image to the top of the screen

def enhance():
    '''
    Will enhance the edges of the image
    :return: Nothing
    '''
    global photoShopImage  # Sends in the image variable being edited, only the B&W needs original image IDK why
    photoShopImage = photoShopImage.filter(ImageFilter.EDGE_ENHANCE)  # Applies edge enhance filter
    photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
    label.configure(image=photoSIE, height = widthI, width = widthI )  # Reconfigures the image on the label
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Sends the image to the top of the screen

def sharpen():
    '''
    Will sharpen the image
    :return: Nothing
    '''
    global photoShopImage  # Sends in the image variable being edited, only the B&W needs original image IDK why
    photoShopImage = photoShopImage.filter(ImageFilter.SHARPEN)  # Sharpens the image
    photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
    label.configure(image=photoSIE, height = widthI, width = widthI )  # Reconfigures the image on the label
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Sends the image to the top of the screen

def contour():
    '''
    Will contour the image
    :return: Nothing
    '''
    global photoShopImage  # Sends in the image variable being edited, only the B&W needs original image IDK why
    photoShopImage = photoShopImage.filter(ImageFilter.CONTOUR) # Enhances all sharp lines in an image
    photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
    label.configure(image=photoSIE, height = widthI, width = widthI )  # Reconfigures the image on the label
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Sends the image to the top of the screen

def rotate():
    '''
    Will rotate the image 90 degrees when clicked
    :return: Nothing
    '''
    global photoShopImage, countR  # Sends in the image variable being edited, only the B&W needs original image IDK why
    if countR%2 == 0:
        photoShopImage = photoShopImage.rotate(90*countR)
        photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
        label.configure(image=photoSIE, height=widthI, width=widthI)  # Reconfigures the image on the label

    else:
        photoShopImage = photoShopImage.rotate(90 * countR) # Rotates the image
        photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
        label.configure(image=photoSIE, height = widthI, width = heightI)  # Reconfigures the image on the label
        label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Sends the image to the top of the screen
    countR += 1
    photoShopImage = photoShopImage = Image.open("Flowers1.jpg")


# Button for Black and White
# Where the button is made, the command for what happens when button is clicked, the text displayed ont the button)
buttonBW = Button(root, command=blackAndWhite, text="Black and White")
buttonBW.pack(padx=2, pady=1, side=LEFT,)  # Sends the button to the bottom of the screen, with space between buttons

# Button for Reseting to Original Image
buttonCLR = Button(root, command=original, text="Reset")
buttonCLR.pack(padx=2, pady=1, side=RIGHT)

# Button for Blur
buttonBLR = Button(root, command=blur, text="Blur")
buttonBLR.pack(padx=2, pady=1, side=LEFT)

# Button for Edge Enhancement
buttonBLR = Button(root, command=enhance, text="Edge Enhancement")
buttonBLR.pack(padx=2, pady=1, side=LEFT)

#Button for Sharpening the Image
buttonSHARP = Button(root, command=sharpen, text="Sharpen")
buttonSHARP.pack(padx=2, pady=1, side=LEFT)

#Button for Contrast
buttonCON = Button(root, command=contour, text="Contour")
buttonCON.pack(padx=2, pady=1, side=LEFT)

#Button for Rotating
buttonRTT = Button(root, command = rotate, text = "Rotate")
buttonRTT.pack(padx = 2, pady = 1, side = BOTTOM)

# This runs the program in an infinite loop until the user closes the window
mainloop()
