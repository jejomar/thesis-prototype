import random
import string
import sys
from tkinter import *
import cv2
import mediapipe as mp
import numpy as np
import pickle
import time
from PIL import Image, ImageTk

letterpred = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

def getRan():
    setLet = random.sample(string.ascii_uppercase, 5)
    return setLet

with open("model.pkl", "rb") as f:
    svm = pickle.load(f)

# Displays the random letters
def display_letter():
    letter = Frame(scrlevone, width=1536, height=216).place(x=0, y=0)
    Label(letter, text="Visual Acuity Assessment Device", font=("Century Gothic", 50, "bold"), fg="black").grid(row=0, column=0)
    for i in range(len(rone)):
        letDisp = Label(letter, text=rone[i], font=("Courier", 150, "bold"), fg="black")
        letDisp.pack(side=LEFT, expand=TRUE)
        #letDisp.grid(row=1, column=i, ipadx=125)

class handDetector():
    def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return lmlist

def image_processed(hand_img):
    global output
    img_rgb = cv2.cvtColor(
        hand_img, cv2.COLOR_BGR2RGB
    )  # 1. Convert BGR to RGB
    # img_flip = cv2.flip(img_rgb, 1)  # 2. Flip the img in Y-axis

    mp_hands = mp.solutions.hands  # Accessing MediaPipe solutions

    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.8,
        model_complexity=1,
        min_tracking_confidence=0.8,
    )  # Initialize Hands

    output = hands.process(img_rgb)  # Results
    hands.close()

    try:
        data = output.multi_hand_landmarks[0]
        data = str(data)
        data = data.strip().split("\n")
        garbage = [
            "landmark {",
            "  visibility: 0.0",
            "  presence: 0.0",
            "}",
        ]
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

def camdisplay():
    TIMER = int(5)
    count = 0
    detector = handDetector()

    success, img = cap.read()
    data = image_processed(img)
    data = np.array(data)
    y_pred = svm.predict(data.reshape(-1, 63))
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)

    if len(img) != 0:
        prev = time.time()

        while TIMER >= 0:
            ret, img = cap.read()

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(y_pred[0]), (25, 75), font,
                        2, (0, 0, 0),
                        2, cv2.LINE_AA)
            cv2.waitKey(125)
            cur = time.time()

            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER - 1
        else:
            verif = str(y_pred[0])

            if verif == rone[count]:
                cv2.imshow('Correct', img)
            else:
                cv2.imshow('Wrong', img)

    frameRGBA = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    imgx = Image.fromarray(frameRGBA)
    imgtk = ImageTk.PhotoImage(image=imgx)
    vidCap.imgtk = imgtk
    vidCap.configure(image=imgtk)
    vidCap.after(20, camdisplay)

    TIMER = int(5)

#Level Start
rone = getRan()

print(rone)
scrlevone = Tk()
scrlevone.title("Screen")
screen_width = scrlevone.winfo_screenwidth()
screen_height = scrlevone.winfo_screenheight()
print(screen_width, screen_height)
scrlevone.geometry("%dx%d+0+0" % (screen_width, screen_height))
scrlevone.overrideredirect(1)

scrlevone.pack_propagate(0)
scrlevone.rowconfigure([0,1,2,3], minsize=307.2)
scrlevone.columnconfigure([0,1,2,3,4], minsize=216)

# For camera display onto the GUI.
vidCap = Label(scrlevone)
vidCap.place(relx=1, rely=1, x=0, y=0, anchor="se")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width, height = 320, 240
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

ign, frame = cap.read()


camdisplay()
display_letter()
scrlevone.mainloop()
