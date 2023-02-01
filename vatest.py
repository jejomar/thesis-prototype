import pickle
import random
import string
from tkinter import *
from tkinter import ttk

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Globally accessible variables
detected_letters = []
random_letters = []
camera_width = 320
camera_height = 240

# Constants
LEVEL_ONE_FONT = ("Courier", 200, "bold")


def main():
    # Define self as global variable
    global main

    # Define root frame
    main = Tk()

    # Define window geometry variables
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # Setup the root frame window
    main.title(
        "Visual Acuity Assessment Device for Mute and/or Mute Individuals"
    )
    main.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main.overrideredirect(0)

    lblTitle = Label(
        main,
        text="Visual Acuity Assessment Device for Mute\n"
        "and or Deaf/Mute Individuals",
        font=("Arial Black", 40),
    )
    lblTitle.pack(ipady=250, fill=X)
    lblGuide = Label(
        main, text="Press the button to start...", font=("Century Gothic", 10)
    )
    lblGuide.pack(ipady=5, fill=X)
    btnStart = ttk.Button(main, text="Start", command=lambda: level_one())
    btnStart.pack(ipadx=50, ipady=10)

    # Run the main() function
    main.mainloop()


def level_one():  # Define self as global variable
    global run_level_one

    # Withdraw main frame
    main.withdraw()

    # Create a frame for the current level
    run_level_one = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_one.winfo_screenwidth()
    screen_height = run_level_one.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # Generate the random letters
    def gen_ran_letters():
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

        random_letters = random.sample(letters_list, 5)
        return random_letters

    # Run the generate function and set it to the global list 'random_letters'
    random_letters = gen_ran_letters()
    print(random_letters)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global letter_frame

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_one, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Iterate through the list of random_letters
        for i in range(len(random_letters)):
            letters = Label(
                letter_frame, text=random_letters[i], font=LEVEL_ONE_FONT
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_one, width=camera_width, height=camera_height, bg="blue"
    )
    camera_frame.pack(side=BOTTOM, fill=X)

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

    # Open the svm model
    with open("model.pkl", "rb") as f:
        svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_one)
    # cam_feed.pack(anchor=SE)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    # Configure OpenCV
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Function for the OpenCV
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
        cam_feed.configure(image=imgtk)
        cam_feed.after(5, camera_display)

    camera_display()


main()
