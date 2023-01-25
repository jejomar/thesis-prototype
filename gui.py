import random
import string
from tkinter import *
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk

def getRan(count):
    setLet = random.sample(string.ascii_uppercase, count)
    return setLet

# Displays the random letters
def display_letter():
    letter = Frame(scrlevone, width=1920, height=300, bg='blue').place(x=0, y=30)

    for i in range(len(rone)):
        letDisp = Label(
            letter, text=rone[i], font=("Courier", 150, "bold"), fg="black"
        )
        letDisp.grid(row=2, column=i)

def image_processed(hand_img):
    img_rgb = cv2.cvtColor(hand_img, cv2.COLOR_BGR2RGB) # 1. Convert BGR to RGB
    img_flip = cv2.flip(img_rgb, 1) # 2. Flip the img in Y-axis
    mp_hands = mp.solutions.hands # Accessing MediaPipe solutions
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.7) # Initialize Hands
    output = hands.process(img_flip) # Results
    hands.close()

    try:
        data = output.multi_hand_landmarks[0]
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

def camdisplay():
    global y_pred
    ign, frame = cap.read()
    data = image_processed(frame)
    data = np.array(data)
    y_pred = svm.predict(data.reshape(-1, 63))
    print(y_pred)

    cv2.putText(frame, str(y_pred[0]), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2, cv2.LINE_AA)
    frameRGBA = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(frameRGBA)
    imgtk = ImageTk.PhotoImage(image = img)
    vidCap.imgtk = imgtk
    vidCap.configure(image=imgtk)
    vidCap.after(10, camdisplay)

camdisplay()
display_letter()
scrlevone.mainloop()