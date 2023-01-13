import random
import string
import sys
from tkinter import *

import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from PIL import Image, ImageTk


def getRan(count):
    setLet = random.sample(string.ascii_uppercase, count)
    return setLet


def image_processed(hand_img):

    # Image processing
    # 1. Convert BGR to RGB
    img_rgb = cv2.cvtColor(hand_img, cv2.COLOR_BGR2RGB)

    # 2. Flip the img in Y-axis
    img_flip = cv2.flip(img_rgb, 1)

    # accessing MediaPipe solutions
    mp_hands = mp.solutions.hands

    # Initialize Hands
    hands = mp_hands.Hands(
        static_image_mode=True, max_num_hands=1, min_detection_confidence=0.7
    )

    # Results
    output = hands.process(img_flip)

    hands.close()

    try:
        data = output.multi_hand_landmarks[0]
        # print(data)
        data = str(data)

        data = data.strip().split("\n")

        garbage = ["landmark {", "  visibility: 0.0", "  presence: 0.0", "}"]

        without_garbage = []

        for i in data:
            if i not in garbage:
                without_garbage.append(i)

        clean = []

        for i in without_garbage:
            i = i.strip()
            clean.append(i[2:])

        for i in range(0, len(clean)):
            clean[i] = float(clean[i])
        return clean
    except:
        return np.zeros([1, 63], dtype=int)[0]


import pickle

# load model
with open("model.pkl", "rb") as f:
    svm = pickle.load(f)


rone = getRan(3)

scrlevone = Tk()
scrlevone.title("Level 1")
screen_width = scrlevone.winfo_screenwidth()
screen_height = scrlevone.winfo_screenheight()
print(screen_width, screen_height)
scrlevone.geometry("%dx%d+0+0" % (screen_width, screen_height))
scrlevone.overrideredirect(1)

# For camera display onto the GUI.
vidCap = Label(scrlevone)
vidCap.place(relx=1, rely=1, x=0, y=0, anchor="se")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width, height = 320, 240
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def show_frames():
    # Get the latest frame and convert into Image
    ret, frame = cap.read()

    # frame = cv.flip(frame,1)
    data = image_processed(frame)
    # print(data.shape)
    data = np.array(data)
    y_pred = svm.predict(data.reshape(-1, 63))
    print(y_pred)

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # org
    org = (50, 100)
    # fontScale
    fontScale = 3
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 5

    cv2.putText(
        frame,
        str(y_pred[0]),
        org,
        font,
        fontScale,
        color,
        thickness,
        cv2.LINE_AA,
    )

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
