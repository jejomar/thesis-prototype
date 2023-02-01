import pickle
import random
import string
import tkinter as tk
from tkinter import ttk

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk

# Constants
HEADER_FONT = ("Century Gothic", 42, "bold")
LETTER_FONT = ("Courier", 200, "bold")
cam_width = 320
cam_height = 240

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


class VATest(tk.Tk):
    def __init__(self, *args, **kwargs):

        # Initialize Tkinter
        tk.Tk.__init__(self, *args, **kwargs)

        # Set window geometry
        tk.Tk.wm_title(self, "Visual Acuity Assessment Tool")

        # Setup the container
        container = tk.Frame(self)
        container.pack()
        container.rowconfigure(0, weight=0)
        container.columnconfigure(0, weight=0)

        # Setup the dictionary for the different frames
        self.frames = {}

        # Uncomment below when there are more frames to be loaded.
        # for F in (Home, LevelOne):
        #     frame = F(container, self)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")

        frame = LevelOne(container, self)
        self.frames[LevelOne] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LevelOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LevelOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Initialize the outer frame
        outer = tk.Frame(self).place(x=0, y=0)
        banner = tk.Label(
            outer, text="Visual Acuity Test: Level 01", font=HEADER_FONT
        )
        banner.place(x=0, y=0)

        # Generate random letters. Use the outer frame as parent
        select = get_random_letters()

        for i in range(len(select)):
            letter = tk.Label(outer, text=select[i], font=LETTER_FONT)

            letter.pack(side="left", expand=True)

        # Setup the camera
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)
        outer = tk.Frame(self)
        outer.tkraise()
        # cam_frame.place(relx=1, rely=1, x=0, y=0, anchor="se")

        # Function for image processing
        def image_processed(hand_img):
            global output
            img_rgb = cv2.cvtColor(
                hand_img, cv2.COLOR_BGR2RGB
            )  # 1. Convert BGR to RGB
            # img_flip = cv2.flip(img_rgb, 1)  # 2. Flip the img in Y-axis

            mp_hands = mp.solutions.hands  # Accessing MediaPipe solutions

            hands = mp_hands.Hands(
                static_image_mode=True,
                max_num_hands=2,
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

        # Load the model
        with open("model.pkl", "rb") as f:
            svm = pickle.load(f)

        # For the camera output
        def camera_display():
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
                    cv2.FONT_HERSHEY_TRIPLEX,
                    2,
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
            outer.imgtk = imgtk
            outer.configure(image=imgtk)
            outer.after(10, camera_display)


def get_random_letters():
    letters_list = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
    ]

    selected = random.sample(letters_list, 5)
    return selected


app = VATest()
app.geometry("1920x1080")
app.mainloop()
