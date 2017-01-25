import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

root = Tk()

imageName = "Flowers3.jpg"


def blackAndWhite():
    '''
    Makes the image black and white
    :return: No return
    '''
    global photoShopImageEdit, photoShopImage  # Imports global image variables to use to edit images
    if photoShopImageEdit == None:  # Only happens if B&W is the first effect, b/c it was blurring automatically
        photoShopImage = photoShopImage.convert("L")  # Converts the image to black and white
        photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
    else:  # If there has been effects applied to the original image
        photoShopImageEdit = photoShopImageEdit.convert("L")
        photoSIE = ImageTk.PhotoImage(photoShopImageEdit)
    label.configure(image=photoSIE)  # Takes the old label and changes the image, reconfigures it
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Puts the image at the top of the screen


def original():
    '''
    Reverts the image back to colour, with no effects
    :return: No return
    '''
    global photoShopImageEdit, photoShopImage  # Sends in the image variables being changed, b/c they need to reset
    photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter
    label.configure(image=photo)  # Reconfigures the label with the original image
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
    label.configure(image=photoSIE)  # Reconfigures the image on the label
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
    label.configure(image=photoSIE)  # Reconfigures the image on the label
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
    label.configure(image=photoSIE)  # Reconfigures the image on the label
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Sends the image to the top of the screen


def contour():
    '''
    Will contour the image
    :return: Nothing
    '''
    global photoShopImage  # Sends in the image variable being edited, only the B&W needs original image IDK why
    photoShopImage = photoShopImage.filter(ImageFilter.CONTOUR)  # Enhances all sharp lines in an image
    photoSIE = ImageTk.PhotoImage(photoShopImage)  # Makes the image compatible with Tkinter
    label.configure(image=photoSIE)  # Reconfigures the image on the label
    label.image = photoSIE  # Saves the edited image so it doesn't get lost
    label.pack(side=TOP)  # Sends the image to the top of the screen


pic = Image.open(imageName)  # This opens the image using the PIL, it doesn't make the image usable in Tkinter
photoShopImage = Image.open(imageName)  # Opens the same image, but so that it is compatible with PIL
photoShopImageEdit = None  # Empty variable to test if any effects have been applied

widthI, heightI = photoShopImage.size # Finds the width and height of the original image

if widthI < 800: # If the width of the image is small
    widthI *= 4
    heightI *= 4
elif heightI < 800: # If the height is also too small
    widthI *= 4
    heightI *= 4

if widthI > heightI or widthI == heightI: # If the image is too large, Landscape or Square image
    while widthI > 800:
        widthI /= 2
        heightI /= 2
elif widthI < heightI: # If the image is in portrait mode
    while heightI > 600:
        widthI /= 2
        heightI /= 2

widthI = int(widthI) # Takes the integer value of the width
heightI = int(heightI) # Takes the integer value of the height
pic = pic.resize((widthI, heightI)) # Resizes the picture to the new width and height
photoShopImage = photoShopImage.resize((widthI, heightI)) # Resizes the editting image to the new width and height

photo = ImageTk.PhotoImage(pic)  # Uses a function in the Image library ImageTk to make it compatible with Tkinter
root.geometry(str(widthI + 60) + 'x' + str(heightI + 60) + '+30+30')  # This sets the screen size (widthxheight+sidePadding+sidePadding)

# Frames
topFrame = Frame(root)  # Frame for image
topFrame.pack()
bottomFrame = Frame(root)  # Frame for buttons
bottomFrame.pack(side=BOTTOM)
label = Label(topFrame, image=photo, height=heightI, width=widthI)  # Creates a label with an image on it
label.image = photo  # Saves the image used in a separate place so it doesn't get overwritten
label.pack(side=TOP)  # Send the image and centres it on the side indicated

# Button for Black and White
# Button(Where the button is made, the command for what happens when button is clicked, the text displayed ont the button)
buttonBW = Button(bottomFrame, command=blackAndWhite, text="Black and White")
buttonBW.pack(padx=2, pady=1,
              side=LEFT, )  # Sends the button to the bottom of the screen, with space between buttons

# Button for Resetting to Original Image
buttonCLR = Button(bottomFrame, command=original, text="Reset")
buttonCLR.pack(padx=2, pady=1, side=RIGHT)

# Button for Blur
buttonBLR = Button(bottomFrame, command=blur, text="Blur")
buttonBLR.pack(padx=2, pady=1, side=LEFT)

# Button for Edge Enhancement
buttonBLR = Button(bottomFrame, command=enhance, text="Edge Enhancement")
buttonBLR.pack(padx=2, pady=1, side=LEFT)

# Button for Sharpening the Image
buttonSHARP = Button(bottomFrame, command=sharpen, text="Sharpen")
buttonSHARP.pack(padx=2, pady=1, side=LEFT)

# Button for Contrast
buttonCON = Button(bottomFrame, command=contour, text="Contour")
buttonCON.pack(padx=2, pady=1, side=LEFT)

# This runs the program in an infinite loop until the user closes the window
root.mainloop()


'''
filter #

im.filter(filter) ⇒ image

Returns a copy of an image filtered by the given filter. For a list of available filters, see the ImageFilter module.
'''