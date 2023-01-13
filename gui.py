import random
import string
import sys
from tkinter import *

import cv2
from PIL import Image, ImageTk


def getRan(count):
    setLet = random.sample(string.ascii_uppercase, count)
    return setLet


rone = getRan(3)

scrlevone = Tk()
scrlevone.title("Level 1")
screen_width = scrlevone.winfo_screenwidth()
screen_height = scrlevone.winfo_screenheight()
print(screen_width, screen_height)
scrlevone.geometry("%dx%d+0+0" % (screen_width, screen_height))
scrlevone.overrideredirect(1)

# For camera displaying
vidCap = Label(scrlevone)
vidCap.place(relx=1, rely=1, x=0, y=0, anchor="se")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width, height = 320, 240
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def show_frames():
    # Get the latest frame and convert into Image
    _, frame = cap.read()
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    vidCap.imgtk = imgtk
    vidCap.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    vidCap.after(20, show_frames)


show_frames()

letter = Frame(scrlevone, width=1920, height=680).place(x=0, y=0)


for i in range(len(rone)):
    label2 = Label(
        letter, text=rone[i], font=("Courier", 150, "bold"), fg="black"
    )
    # label2.config(anchor=CENTER)
    label2.pack(side=LEFT, fill=X, ipadx=10, ipady=10, expand=TRUE)


scrlevone.mainloop()
