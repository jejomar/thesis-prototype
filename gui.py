import pickle
import random
import string
from tkinter import *

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk

cd = int(5)

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def getRan():
    setLet = random.sample(string.ascii_uppercase, 5)
    return setLet


# Displays the random letters
def display_letter():
    letter = Frame(scrlevone, width=1536, height=216, bg="blue").place(
        x=0, y=0
    )
    Label(
        letter,
        text="Visual Acuity Assessment Device",
        font=("Century Gothic", 50, "bold"),
        fg="black",
    ).grid(row=0, column=0)
    for i in range(len(rone)):
        letDisp = Label(
            letter, text=rone[i], font=("Courier", 150, "bold"), fg="black"
        )
        letDisp.pack(side=LEFT, expand=TRUE)
        # letDisp.grid(row=1, column=i, ipadx=125)


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


with open("model.pkl", "rb") as f:
    svm = pickle.load(f)

rone = getRan()

scrlevone = Tk()
scrlevone.title("Level 1")
screen_width = scrlevone.winfo_screenwidth()
screen_height = scrlevone.winfo_screenheight()
print(screen_width, screen_height)
scrlevone.geometry("%dx%d+0+0" % (screen_width, screen_height))
scrlevone.overrideredirect(1)

scrlevone.pack_propagate(0)
scrlevone.rowconfigure([0, 1, 2, 3], minsize=307.2)
scrlevone.columnconfigure([0, 1, 2, 3, 4], minsize=216)

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

    # Will only get the detected letter only if hands are present in the frame.
    if (
        output.multi_hand_landmarks
    ):  # Line checks if hands are present in the frame
        data = np.array(data)
        y_pred = svm.predict(data.reshape(-1, 63))
        print(y_pred)

        cv2.putText(
            frame,
            str(y_pred[0]),
            (20, 50),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255, 0, 0),
            2,
            cv2.LINE_AA,
        )

        # Draw the hand annotations on the image
        img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if output.multi_hand_landmarks:
            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

    frameRGBA = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(frameRGBA)
    imgtk = ImageTk.PhotoImage(image=img)
    vidCap.imgtk = imgtk
    vidCap.configure(image=imgtk)
    vidCap.after(10, camdisplay)


camdisplay()
display_letter()
scrlevone.mainloop()
