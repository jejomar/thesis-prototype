import datetime
import os
import pickle
import random
from tkinter import *
from tkinter import ttk

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageGrab, ImageTk

# Globally accessible variables
detected_letters1 = []
detected_letters2 = []
detected_letters3 = []
detected_letters4 = []
detected_letters5 = []
detected_letters6 = []
detected_letters7 = []
detected_letters8 = []
detected_letters9 = []
detected_letters10 = []

score1 = "---"
score2 = "---"
score3 = "---"
score4 = "---"
score5 = "---"
score6 = "---"
score7 = "---"
score8 = "---"
score9 = "---"
score10 = "---"

camera_width = 320
camera_height = 240

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Open the svm model
with open("model.pkl", "rb") as f:
    svm = pickle.load(f)

# Constants
CUE_FONT = ("Montserrat SemiBold", 45)

# Start the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

######################
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
        "J",
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
        "Z",
    ]

    random_letters = random.sample(letters_list, 5)
    return random_letters


######################

######################
def returnTitle():
    levselScreen.withdraw()
    main.deiconify()


def returnLevSel():
    eyeScreen.withdraw()
    main.deiconify()


def returnLEye():
    leinstrScreen.withdraw()
    main.deiconify()


def returnREye():
    reinstrScreen.withdraw()
    main.deiconify()


def returnBEye():
    beinstrScreen.withdraw()
    main.deiconify()


######################

######################
def eyeChosen(eye):
    global chosenEye

    chosenEye = eye

    if eye == "left":
        eyeScreen.withdraw()
        lefteyeinstr()
    elif eye == "right":
        eyeScreen.withdraw()
        righteyeinstr()
    else:
        eyeScreen.withdraw()
        botheyeinstr()


######################

######################
def lvlChosen():
    if chosenEye == "left":
        if chosenLvl == "one":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_one()
        elif chosenLvl == "two":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_two()
        elif chosenLvl == "thr":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_three()
        elif chosenLvl == "fou":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_four()
        elif chosenLvl == "fiv":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_five()
        elif chosenLvl == "six":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_six()
        elif chosenLvl == "sev":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_seven()
        elif chosenLvl == "eig":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_eight()
        elif chosenLvl == "nin":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_nine()
        else:
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_ten()
    elif chosenEye == "right":
        if chosenLvl == "one":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_one()
        elif chosenLvl == "two":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_two()
        elif chosenLvl == "thr":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_three()
        elif chosenLvl == "fou":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_four()
        elif chosenLvl == "fiv":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_five()
        elif chosenLvl == "six":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_six()
        elif chosenLvl == "sev":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_seven()
        elif chosenLvl == "eig":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_eight()
        elif chosenLvl == "nin":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_nine()
        else:
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_ten()

    else:
        if chosenLvl == "one":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_one()
        elif chosenLvl == "two":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_two()
        elif chosenLvl == "thr":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_three()
        elif chosenLvl == "fou":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_four()
        elif chosenLvl == "fiv":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_five()
        elif chosenLvl == "six":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_six()
        elif chosenLvl == "sev":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_seven()
        elif chosenLvl == "eig":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_eight()
        elif chosenLvl == "nin":
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_nine()
        else:
            beinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_ten()


######################

######################
def levelselect():
    global levselScreen
    main.withdraw()

    levselScreen = Toplevel(main)
    screen_width = levselScreen.winfo_screenwidth()
    screen_height = levselScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    levselScreen.title(
        "Visual Acuity Assessment Device for Mute and/or Mute Individuals"
    )
    levselScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    levselScreen.overrideredirect(0)
    levselScreen.pack_propagate(0)

    btnReturn = ttk.Button(
        levselScreen, text="Return", command=lambda: returnTitle()
    )
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(
        levselScreen,
        text="— LEVEL SELECT —",
        font=("Montserrat ExtraBold", 40),
    )
    lblTitle.pack(fill=X)
    lblInstr = Label(
        levselScreen,
        text="Select the level to start the assessment.",
        font=("Montserrat", 15),
    )
    lblInstr.pack(fill=X)

    frmTop = Frame(levselScreen, width=width, height=(height - 45))
    frmTop.pack(fill=X, pady=(15, 5))
    frmBot = Frame(levselScreen, width=width, height=(height - 45))
    frmBot.pack(fill=X, pady=(5, 15))

    one = PhotoImage(file=r"Buttons\20_200.png")
    two = PhotoImage(file=r"Buttons\20_120.png")
    thr = PhotoImage(file=r"Buttons\20_80.png")
    fou = PhotoImage(file=r"Buttons\20_60.png")
    fiv = PhotoImage(file=r"Buttons\20_40.png")
    six = PhotoImage(file=r"Buttons\20_30.png")
    sev = PhotoImage(file=r"Buttons\20_20.png")
    eig = PhotoImage(file=r"Buttons\20_15.png")
    nin = PhotoImage(file=r"Buttons\20_13.png")
    ten = PhotoImage(file=r"Buttons\20_10.png")

    btnLevel1 = ttk.Button(
        frmTop, text="Level 1", image=one, command=lambda: eyetest("one")
    )
    btnLevel1.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel2 = ttk.Button(
        frmTop, text="Level 2", image=two, command=lambda: eyetest("two")
    )
    btnLevel2.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel3 = ttk.Button(
        frmTop, text="Level 3", image=thr, command=lambda: eyetest("thr")
    )
    btnLevel3.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel4 = ttk.Button(
        frmTop, text="Level 4", image=fou, command=lambda: eyetest("fou")
    )
    btnLevel4.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel5 = ttk.Button(
        frmTop, text="Level 5", image=fiv, command=lambda: eyetest("fiv")
    )
    btnLevel5.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel6 = ttk.Button(
        frmBot, text="Level 6", image=six, command=lambda: eyetest("six")
    )
    btnLevel6.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel7 = ttk.Button(
        frmBot, text="Level 7", image=sev, command=lambda: eyetest("sev")
    )
    btnLevel7.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel8 = ttk.Button(
        frmBot, text="Level 8", image=eig, command=lambda: eyetest("eig")
    )
    btnLevel8.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel9 = ttk.Button(
        frmBot, text="Level 9", image=nin, command=lambda: eyetest("nin")
    )
    btnLevel9.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)
    btnLevel10 = ttk.Button(
        frmBot, text="Level 10", image=ten, command=lambda: eyetest("ten")
    )
    btnLevel10.pack(side=LEFT, padx=29, pady=25, ipadx=34, ipady=30)

    levselScreen.mainloop()


######################

######################
def eyetest(level):
    global eyeScreen
    global chosenLvl
    levselScreen.withdraw()

    chosenLvl = level

    left = PhotoImage(file=r"Buttons\lefteye.png")
    right = PhotoImage(file=r"Buttons\righteye.png")
    both = PhotoImage(file=r"Buttons\botheye.png")

    eyeScreen = Toplevel(main)
    screen_width = eyeScreen.winfo_screenwidth()
    screen_height = eyeScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    eyeScreen.title(
        "Visual Acuity Assessment Device for Mute and/or Mute Individuals"
    )
    eyeScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    eyeScreen.overrideredirect(0)
    eyeScreen.pack_propagate(0)

    btnReturn = ttk.Button(
        eyeScreen, text="Return", command=lambda: returnLevSel()
    )
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(
        eyeScreen, text="— EYE TO TEST —", font=("Montserrat ExtraBold", 40)
    )
    lblTitle.pack(fill=X)
    lblInstr = Label(
        eyeScreen,
        text="Select which eye will be tested.",
        font=("Montserrat", 15),
    )
    lblInstr.pack(fill=X)

    frmLeft = Frame(eyeScreen, width=width, height=(height - 45))
    frmLeft.pack(
        side=LEFT, pady=(10, 20), padx=(20, 10), fill=BOTH, expand=TRUE
    )
    frmBoth = Frame(eyeScreen, width=width, height=(height - 45))
    frmBoth.pack(
        side=LEFT, pady=(10, 20), padx=(10, 20), fill=BOTH, expand=TRUE
    )
    frmRight = Frame(eyeScreen, width=width, height=(height - 45))
    frmRight.pack(
        side=LEFT, pady=(10, 20), padx=(10, 20), fill=BOTH, expand=TRUE
    )

    btnLeft = ttk.Button(
        frmLeft,
        text="Left Eye",
        image=left,
        command=lambda: eyeChosen("left"),
    )
    btnLeft.pack(pady=(20, 10), padx=20, fill=BOTH, ipady=100)

    btnBoth = ttk.Button(
        frmBoth,
        text="Both Eye",
        image=both,
        command=lambda: eyeChosen("both"),
    )
    btnBoth.pack(pady=(20, 10), padx=20, fill=BOTH, ipady=100)

    btnRight = ttk.Button(
        frmRight,
        text="Right Eye",
        image=right,
        command=lambda: eyeChosen("right"),
    )
    btnRight.pack(pady=(20, 10), padx=20, fill=BOTH, ipady=100)

    eyeScreen.mainloop()


######################

######################
def lefteyeinstr():
    global leinstrScreen
    levselScreen.withdraw()

    leinstrScreen = Toplevel(main)
    screen_width = leinstrScreen.winfo_screenwidth()
    screen_height = leinstrScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    leinstrScreen.title(
        "Visual Acuity Assessment Device for Mute and/or Mute Individuals"
    )
    leinstrScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    leinstrScreen.overrideredirect(0)
    leinstrScreen.pack_propagate(0)

    btnReturn = ttk.Button(
        leinstrScreen, text="Return", command=lambda: returnLEye()
    )
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(
        leinstrScreen,
        text="— INSTRUCTIONS —",
        font=("Montserrat ExtraBold", 40),
    )
    lblTitle.pack(fill=X)
    lblInstr = Label(
        leinstrScreen,
        text="Please read the following.",
        font=("Montserrat", 15),
    )
    lblInstr.pack(fill=X)

    frmInstruction = Frame(leinstrScreen, width=width, height=(height - 80))
    frmInstruction.pack(fill=BOTH, expand=TRUE)

    lblInstruction = Label(
        frmInstruction,
        text="1. Kindly keep your right eye covered throughout the exam.\n\n"
        "2. Raise only one hand and make sure it's centered in the camera frame.\n\n"
        "3. Read and perform the gestures of the displayed letters one at a time every 5 seconds"
        " and hold the gesture within the given time interval.\n\n"
        "4. As the timer reaches 1 second, prepare for the next letter.\n\n"
        "5. Once done, repeat steps 1 and 4 until all letters are done.",
        font=("Montserrat SemiBold", 24),
        justify=LEFT,
    )
    lblInstruction.bind(
        "<Configure>", lambda e: lblInstruction.config(wraplength=width * 0.95)
    )
    lblInstruction.pack(fill=X, padx=10, pady=(30, 20))

    btnBegin = ttk.Button(
        leinstrScreen, text="Begin", command=lambda: lvlChosen()
    )
    btnBegin.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=E)

    leinstrScreen.mainloop()


######################

######################
def righteyeinstr():
    global reinstrScreen
    levselScreen.withdraw()

    reinstrScreen = Toplevel(main)
    screen_width = reinstrScreen.winfo_screenwidth()
    screen_height = reinstrScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    reinstrScreen.title(
        "Visual Acuity Assessment Device for Mute and/or Mute Individuals"
    )
    reinstrScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    reinstrScreen.overrideredirect(0)
    reinstrScreen.pack_propagate(0)

    btnReturn = ttk.Button(
        reinstrScreen, text="Return", command=lambda: returnREye()
    )
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(
        reinstrScreen,
        text="— INSTRUCTIONS —",
        font=("Montserrat ExtraBold", 40),
    )
    lblTitle.pack(fill=X)
    lblInstr = Label(
        reinstrScreen,
        text="Please read the following.",
        font=("Montserrat", 15),
    )
    lblInstr.pack(fill=X)

    frmInstruction = Frame(reinstrScreen, width=width, height=(height - 80))
    frmInstruction.pack(fill=BOTH, expand=TRUE)

    lblInstruction = Label(
        frmInstruction,
        text="1. Kindly keep your left eye covered throughout the exam.\n\n"
        "2. Raise only one hand and make sure it's centered in the camera frame.\n\n"
        "3. Read and perform the gestures of the displayed letters one at a time every 5 seconds"
        " and hold the gesture within the given time interval.\n\n"
        "4. As the timer reaches 1 second, prepare for the next letter.\n\n"
        "5. Once done, repeat steps 1 and 4 until all letters are done.",
        font=("Montserrat SemiBold", 24),
        justify=LEFT,
    )
    lblInstruction.bind(
        "<Configure>", lambda e: lblInstruction.config(wraplength=width * 0.95)
    )
    lblInstruction.pack(fill=X, padx=10, pady=(30, 20))

    btnBegin = ttk.Button(
        reinstrScreen, text="Begin", command=lambda: lvlChosen()
    )
    btnBegin.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=E)

    reinstrScreen.mainloop()


######################

######################
def botheyeinstr():
    global beinstrScreen
    levselScreen.withdraw()

    beinstrScreen = Toplevel(main)
    screen_width = beinstrScreen.winfo_screenwidth()
    screen_height = beinstrScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    beinstrScreen.title(
        "Visual Acuity Assessment Device for Mute and/or Mute Individuals"
    )
    beinstrScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    beinstrScreen.overrideredirect(0)
    beinstrScreen.pack_propagate(0)

    btnReturn = ttk.Button(
        beinstrScreen, text="Return", command=lambda: returnBEye()
    )
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(
        beinstrScreen,
        text="— INSTRUCTIONS —",
        font=("Montserrat ExtraBold", 40),
    )
    lblTitle.pack(fill=X)
    lblInstr = Label(
        beinstrScreen,
        text="Please read the following.",
        font=("Montserrat", 15),
    )
    lblInstr.pack(fill=X)

    frmInstruction = Frame(beinstrScreen, width=width, height=(height - 80))
    frmInstruction.pack(fill=BOTH, expand=TRUE)

    lblInstruction = Label(
        frmInstruction,
        text="1. Raise only one hand and make sure it's centered in the camera frame.\n\n"
        "2. Read and perform the gestures of the displayed letters one at a time every 5 seconds"
        " and hold the gesture within the given time interval.\n\n"
        "3. As the timer reaches 1 second, prepare for the next letter.\n\n"
        "4. Once done, repeat steps 1 and 3 until all letters are done.",
        font=("Montserrat SemiBold", 24),
        justify=LEFT,
    )
    lblInstruction.bind(
        "<Configure>", lambda e: lblInstruction.config(wraplength=width * 0.95)
    )
    lblInstruction.pack(fill=X, padx=10, pady=(30, 20))

    btnBegin = ttk.Button(
        beinstrScreen, text="Begin", command=lambda: lvlChosen()
    )
    btnBegin.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=E)

    beinstrScreen.mainloop()


######################

######################
def level_one():  # Define self as global variable
    global run_level_one
    global ctr_level_one

    # Create a frame for the current level
    run_level_one = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_one.winfo_screenwidth()
    screen_height = run_level_one.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_one.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
    run_level_one.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_one, width=1920, height=35)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 1 — 20 / 200",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_one
        # Create a frame for the letter generated
        letter_frame = Frame(run_level_one, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_one = ["A", "B", "C", "D", "E"]
        print(random_one)

        # Iterate through the list of random_letters
        for i in range(len(random_one)):
            letters = Label(
                letter_frame, text=random_one[i], font=("Courier", 251, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(run_level_one, width=1980, height=camera_height)
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=30)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_one)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    def image_processed(hand_img):
        global output
        img_rgb = cv2.cvtColor(
            hand_img, cv2.COLOR_BGR2RGB
        )  # 1. Convert BGR to RGB

        img_flip = cv2.flip(img_rgb, 1)  # 2. Flip the img in Y-axis

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

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global frame
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters1) < 5:

            if output.multi_hand_landmarks:
                # This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                # Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                # Ang countdown nya is set to five lang. Pero, kapag may laman na,
                # Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
                if len(detected_letters1) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters1.append(y_pred[0])

                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters1)
                    cv2.waitKey(3000)

                else:
                    cue_label.config(
                        text=str(detected_letters1)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )

            else:

                cue_label.config(
                    text=str(detected_letters1) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)

        # If all detected letters are now stored in the array, program will wait for 3 seconds.
        # before proceeding to the next level
        else:
            if len(detected_letters1) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters1)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cv2.waitKey(10)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score1

        ctr_level_one = 0
        arrlen = len(random_one)
        for i in range(arrlen):
            if detected_letters1[i] == random_one[i]:
                ctr_level_one = ctr_level_one + 1

        if ctr_level_one != 0:
            score1 = str(ctr_level_one) + " / " + str(arrlen)
            print(score1)
            level_two()
            run_level_one.destroy()
        else:
            score1 = str(ctr_level_one) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_one.destroy()


######################

######################
def level_two():  # Define self as global variable
    global run_level_two
    global ctr_level_two

    # Create a frame for the current level
    run_level_two = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_two.winfo_screenwidth()
    screen_height = run_level_two.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_two.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
    run_level_two.overrideredirect(1)

    global start_time
    global finish

    # Generate the random letters
    label_frame = Frame(run_level_two, width=1920, height=35)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 2 — 20 / 120",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_two

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_two, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_two = ["F", "G", "H", "I", "J"]
        print(random_two)

        # Iterate through the list of random_letters
        for i in range(len(random_two)):
            letters = Label(
                letter_frame, text=random_two[i], font=("Courier", 151, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(run_level_two, width=1980, height=camera_height)
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=30)

    # # Function for image processing
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_two)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global frame
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

            # For verfication and time

            # Verification Section

        def verify():
            global score2

            ctr_level_two = 0
            arrlen = len(random_two)
            for i in range(arrlen):
                if detected_letters2[i] == random_two[i]:
                    ctr_level_two = ctr_level_two + 1

            if ctr_level_two != 0:
                score2 = str(ctr_level_two) + " / " + str(arrlen)
                print(score2)
                level_three()
                run_level_two.destroy()
            else:
                score2 = str(ctr_level_two) + " / " + str(arrlen)
                cv2.destroyAllWindows()
                results()
                run_level_two.destroy()

        if len(detected_letters2) < 5:

            if output.multi_hand_landmarks:
                # This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                # Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                # Ang countdown nya is set to five lang. Pero, kapag may laman na,
                # Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
                if len(detected_letters2) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters2.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters2)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters2)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters2) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)

        else:
            if len(detected_letters2) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters2)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()


######################

######################
def level_three():  # Define self as global variable
    global run_level_three
    global ctr_level_three

    # Create a frame for the current level
    run_level_three = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_three.winfo_screenwidth()
    screen_height = run_level_three.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_three.geometry(
        "%dx%d+%d+%d" % (screen_width, screen_height, 0, 0)
    )
    run_level_three.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_three, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 3 — 20 / 80",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_thr

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_three, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_thr = ["K", "L", "M", "N", "O"]
        print(random_thr)

        # Iterate through the list of random_letters
        for i in range(len(random_thr)):
            letters = Label(
                letter_frame, text=random_thr[i], font=("Courier", 101, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(run_level_three, width=1980, height=camera_height)
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=30)

    # # Function for image processing
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_three)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters3) < 5:

            if output.multi_hand_landmarks:
                # This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                # Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                # Ang countdown nya is set to five lang. Pero, kapag may laman na,
                # Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
                if len(detected_letters3) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters3.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters3)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters3)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters3) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters3) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters3)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score3

        ctr_level_three = 0
        arrlen = len(random_thr)
        for i in range(arrlen):
            if detected_letters3[i] == random_thr[i]:
                ctr_level_three = ctr_level_three + 1

        if ctr_level_three != 0:
            score3 = str(ctr_level_three) + " / " + str(arrlen)
            print(score3)
            level_four()
            run_level_three.destroy()
        else:
            score3 = str(ctr_level_three) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_three.destroy()


######################

######################
def level_four():  # Define self as global variable
    global run_level_four
    global ctr_level_four

    # Create a frame for the current level
    run_level_four = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_four.winfo_screenwidth()
    screen_height = run_level_four.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_four.geometry(
        "%dx%d+%d+%d" % (screen_width, screen_height, 0, 0)
    )
    run_level_four.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_four, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 4 — 20 / 60",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_fou

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_four, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_fou = ["P", "Q", "R", "S", "T"]
        print(random_fou)

        # Iterate through the list of random_letters
        for i in range(len(random_fou)):
            letters = Label(
                letter_frame, text=random_fou[i], font=("Courier", 75, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(run_level_four, width=1920, height=camera_height)
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=30)

    # # Function for image processing
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_four)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters4) < 5:

            if output.multi_hand_landmarks:
                if len(detected_letters4) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters4.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters4)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters4)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters4) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters4) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters4)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score4

        ctr_level_four = 0
        arrlen = len(random_fou)
        for i in range(arrlen):
            if detected_letters4[i] == random_fou[i]:
                ctr_level_four = ctr_level_four + 1

        if ctr_level_four != 0:
            score4 = str(ctr_level_four) + " / " + str(arrlen)
            print(score4)
            level_five()
            run_level_four.destroy()
        else:
            score4 = str(ctr_level_four) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_four.destroy()


######################

######################
def level_five():  # Define self as global variable
    global run_level_five
    global ctr_level_five

    # Create a frame for the current level
    run_level_five = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_five.winfo_screenwidth()
    screen_height = run_level_five.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_five.geometry(
        "%dx%d+%d+%d" % (screen_width, screen_height, 0, 0)
    )
    run_level_five.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_five, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 5 — 20 / 40",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_five

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_five, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_five = ["U", "V", "W", "X", "Y"]
        print(random_five)

        # Iterate through the list of random_letters
        for i in range(len(random_five)):
            letters = Label(
                letter_frame, text=random_five[i], font=("Courier", 50, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(run_level_five, width=1980, height=camera_height)
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=30)

    # # Function for image processing
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_five)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters5) < 5:

            if output.multi_hand_landmarks:
                # This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                # Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                # Ang countdown nya is set to five lang. Pero, kapag may laman na,
                # Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
                if len(detected_letters5) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters5.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters5)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters5)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters5) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters5) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters5)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score5

        ctr_level_five = 0
        arrlen = len(random_five)
        for i in range(arrlen):
            if detected_letters5[i] == random_five[i]:
                ctr_level_five = ctr_level_five + 1

        if ctr_level_five != 0:
            score5 = str(ctr_level_five) + " / " + str(arrlen)
            print(score5)
            level_six()
            run_level_five.destroy()
        else:
            score5 = str(ctr_level_five) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_five.destroy()


######################

######################
def level_six():  # Define self as global variable
    global run_level_six
    global ctr_level_six

    # Create a frame for the current level
    run_level_six = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_six.winfo_screenwidth()
    screen_height = run_level_six.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_six.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
    run_level_six.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_six, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 6 — 20 / 30",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_six

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_six, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_six = ["Z", "A", "B", "C", "D"]
        print(random_six)

        # Iterate through the list of random_letters
        for i in range(len(random_six)):
            letters = Label(
                letter_frame, text=random_six[i], font=("Courier", 38, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(run_level_six, width=1920, height=camera_height)
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=10)

    # # Function for image processing
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
            min_detection_confidence=0.7,
            model_complexity=1,
            min_tracking_confidence=0.7,
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_six)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters6) < 5:

            if output.multi_hand_landmarks:
                if len(detected_letters6) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters6.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters6)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters6)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters6) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters6) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters6)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score6

        ctr_level_six = 0
        arrlen = len(random_six)
        for i in range(arrlen):
            if detected_letters6[i] == random_six[i]:
                ctr_level_six = ctr_level_six + 1

        if ctr_level_six != 0:
            score6 = str(ctr_level_six) + " / " + str(arrlen)
            print(score6)
            level_seven()
            run_level_six.destroy()

        else:
            score6 = str(ctr_level_six) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_six.destroy()


######################

######################
def level_seven():  # Define self as global variable
    global run_level_seven
    global ctr_level_seven

    # Create a frame for the current level
    run_level_seven = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_seven.winfo_screenwidth()
    screen_height = run_level_seven.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_seven.geometry(
        "%dx%d+%d+%d" % (screen_width, screen_height, 0, 0)
    )
    run_level_seven.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_seven, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 7 — 20 / 20",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_seven

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_seven, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_seven = gen_ran_letters()
        print(random_seven)

        # Iterate through the list of random_letters
        for i in range(len(random_seven)):
            letters = Label(
                letter_frame,
                text=random_seven[i],
                font=("Courier", 25, "bold"),
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(run_level_seven, width=1920, height=camera_height)
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=10)

    # # Function for image processing
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
            min_detection_confidence=0.7,
            model_complexity=1,
            min_tracking_confidence=0.7,
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_seven)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters7) < 5:

            if output.multi_hand_landmarks:
                # This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                # Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                # Ang countdown nya is set to five lang. Pero, kapag may laman na,
                # Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
                if len(detected_letters7) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters7.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters7)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters7)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters7) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters7) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters7)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score7

        ctr_level_seven = 0
        arrlen = len(random_seven)
        for i in range(arrlen):
            if detected_letters7[i] == random_seven[i]:
                ctr_level_seven = ctr_level_seven + 1

        if ctr_level_seven != 0:
            score7 = str(ctr_level_seven) + " / " + str(arrlen)
            print(score7)
            level_eight()
            run_level_seven.destroy()
        else:
            score7 = str(ctr_level_seven) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_seven.destroy()


######################

######################
def level_eight():  # Define self as global variable
    global run_level_eight
    global ctr_level_eight

    # Create a frame for the current level
    run_level_eight = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_eight.winfo_screenwidth()
    screen_height = run_level_eight.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_eight.geometry(
        "%dx%d+%d+%d" % (screen_width, screen_height, 0, 0)
    )
    run_level_eight.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_eight, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 8 — 20 / 15",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_eight

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_eight, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_eight = gen_ran_letters()
        print(random_eight)

        # Iterate through the list of random_letters
        for i in range(len(random_eight)):
            letters = Label(
                letter_frame,
                text=random_eight[i],
                font=("Courier", 19, "bold"),
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_eight, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=10)

    # # Function for image processing
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
            min_detection_confidence=0.7,
            model_complexity=1,
            min_tracking_confidence=0.7,
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_eight)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters8) < 5:

            if output.multi_hand_landmarks:
                if len(detected_letters8) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters8.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters8)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters8)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters8) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters8) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters8)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score8

        ctr_level_eight = 0
        arrlen = len(random_eight)
        for i in range(arrlen):
            if detected_letters8[i] == random_eight[i]:
                ctr_level_eight = ctr_level_eight + 1

        if ctr_level_eight != 0:
            score8 = str(ctr_level_eight) + " / " + str(arrlen)
            print(score8)
            level_nine()
            run_level_eight.destroy()
        else:
            score8 = str(ctr_level_eight) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_eight.destroy()


######################

######################
def level_nine():  # Define self as global variable
    global run_level_nine
    global ctr_level_nine

    # Create a frame for the current level
    run_level_nine = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_nine.winfo_screenwidth()
    screen_height = run_level_nine.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_nine.geometry(
        "%dx%d+%d+%d" % (screen_width, screen_height, 0, 0)
    )
    run_level_nine.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_nine, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 9 — 20 / 13",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_nine

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_nine, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_nine = gen_ran_letters()
        print(random_nine)

        # Iterate through the list of random_letters
        for i in range(len(random_nine)):
            letters = Label(
                letter_frame, text=random_nine[i], font=("Courier", 16, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_nine, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=10)

    # # Function for image processing
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
            min_detection_confidence=0.7,
            model_complexity=1,
            min_tracking_confidence=0.7,
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_nine)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters9) < 5:

            if output.multi_hand_landmarks:
                # This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                # Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                # Ang countdown nya is set to five lang. Pero, kapag may laman na,
                # Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
                if len(detected_letters9) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters9.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters9)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters9)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters9) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters9) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters9)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGRA2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score9

        ctr_level_nine = 0
        arrlen = len(random_nine)
        for i in range(arrlen):
            if detected_letters9[i] == random_nine[i]:
                ctr_level_nine = ctr_level_nine + 1

        if ctr_level_nine != 0:
            score9 = str(ctr_level_nine) + " / " + str(arrlen)
            print(score9)
            level_ten()
            run_level_nine.destroy()
        else:
            score9 = str(ctr_level_nine) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_nine.destroy()


######################

######################
def level_ten():  # Define self as global variable
    global run_level_ten
    global ctr_level_ten

    # Create a frame for the current level
    run_level_ten = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_ten.winfo_screenwidth()
    screen_height = run_level_ten.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_ten.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
    run_level_ten.overrideredirect(1)

    global start_time
    global finish

    label_frame = Frame(run_level_ten, width=1920, height=50)
    label_frame.pack(fill=X)

    lblLevel = Label(
        label_frame,
        text="VISUAL ACUITY ASSESSMENT PROPER                       |",
        font=("Montserrat", 40),
    )
    lblLevel.pack(side=LEFT, padx=(20, 0), pady=10, anchor=W)
    lblIndic = Label(
        label_frame,
        text="Level 10 — 20 / 10",
        font=("Montserrat ExtraBold", 40),
    )
    lblIndic.pack(side=RIGHT, padx=(0, 20), pady=10, anchor=W)

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_ten

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_ten, width=1920, height=670)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_ten = gen_ran_letters()
        print(random_ten)

        # Iterate through the list of random_letters
        for i in range(len(random_ten)):
            letters = Label(
                letter_frame, text=random_ten[i], font=("Courier", 13, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_ten, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(camera_frame, text=" ", font=CUE_FONT)
    cue_label.pack(side=LEFT, padx=30, pady=10)

    # # Function for image processing
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
            min_detection_confidence=0.7,
            model_complexity=1,
            min_tracking_confidence=0.7,
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

    # # Open the svm model
    # with open("model.pkl", "rb") as f:
    #     svm = pickle.load(f)

    # Display the camera feed in the GUI
    cam_feed = Label(run_level_ten)
    cam_feed.place(relx=1, rely=1, x=0, y=0, anchor="se")

    start_time = datetime.datetime.now()
    print(f"Start: {start_time}")

    finish = start_time + datetime.timedelta(seconds=5)
    print(f"Finish: {finish.isoformat()}")

    # Function for the OpenCV
    def camera_display():
        global y_pred
        global start_time
        global finish

        curr = datetime.datetime.now()

        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

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
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 0, 0),
                15,
                cv2.LINE_AA,
            )

            # Draw the hand annotations on the image
            img_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            print(f"Start: {start_time.isoformat()}")
            print(f"Finish: {finish.isoformat()}")
            print(f"Current: {curr.isoformat()}")

        if len(detected_letters10) < 5:

            if output.multi_hand_landmarks:
                # This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                # Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                # Ang countdown nya is set to five lang. Pero, kapag may laman na,
                # Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
                if len(detected_letters10) == 0:
                    countdown = 5
                else:
                    countdown = 8

                if (int((curr - start_time).total_seconds())) is countdown:
                    detected_letters10.append(y_pred[0])
                    start_time = curr
                    curr = datetime.datetime.now()
                    finish = start_time + datetime.timedelta(seconds=5)
                    print(detected_letters10)
                    cv2.waitKey(3000)
                else:
                    cue_label.config(
                        text=str(detected_letters10)
                        + " | Hold the gesture for "
                        + str(
                            countdown
                            - int((curr - start_time).total_seconds())
                        )
                        + " second/s."
                    )
            else:
                cue_label.config(
                    text=str(detected_letters10) + " | No hands detected."
                )
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
            if len(detected_letters10) == 5:

                print(f"Start: {start_time.isoformat()}")
                print(f"Finish: {finish.isoformat()}")
                print(f"Current: {curr.isoformat()}")

                cue_label.config(
                    text=str(detected_letters10)
                    + " | Please wait for "
                    + str(5 - int((curr - start_time).total_seconds()))
                    + " second/s."
                )

                if (int((curr - start_time).total_seconds())) is 5:
                    verify()

        frameRGB = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frameRGB)
        imgtk = ImageTk.PhotoImage(image=img)
        cam_feed.configure(image=imgtk)
        cam_feed.after(10, camera_display)

        cv2.imshow("Feed", frame)  # This works though?
        cv2.setWindowProperty("Feed", cv2.WND_PROP_TOPMOST, 1)
        cv2.moveWindow("Feed", 1595, 810)

    camera_display()

    def verify():
        global score10

        ctr_level_ten = 0
        arrlen = len(random_ten)
        for i in range(arrlen):
            if detected_letters10[i] == random_ten[i]:
                ctr_level_ten = ctr_level_ten + 1

        if ctr_level_ten != 0:
            score10 = str(ctr_level_ten) + " / " + str(arrlen)
            print(score10)
            results()
            run_level_ten.destroy()
        else:
            score10 = str(ctr_level_ten) + " / " + str(arrlen)
            cv2.destroyAllWindows()
            results()
            run_level_ten.destroy()


######################

######################
def results():  # Define self as global variable
    global resultsScreen
    global score1
    global score2
    global score3
    global score4
    global score5
    global score6
    global score7
    global score8
    global score9
    global score10
    global entName
    global btnFinish

    # Cleanup webcam feed
    # cap.release()
    # cv2.destroyAllWindows()

    # Create a frame for the current level
    resultsScreen = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = resultsScreen.winfo_screenwidth()
    screen_height = resultsScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    resultsScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    resultsScreen.overrideredirect(0)

    lblTitle = Label(
        resultsScreen,
        text="— ASSESSMENT RESULTS —",
        font=("Montserrat ExtraBold", 40),
    )
    lblTitle.pack(fill=X, pady=(30, 0))
    lblInstr = Label(
        resultsScreen,
        text="Here's the results of the completed assessment.",
        font=("Montserrat", 15),
    )
    lblInstr.pack(fill=X)

    frmBottom = Frame(resultsScreen, width=width, height=10)
    frmBottom.pack(side=BOTTOM, padx=10, pady=10, fill=X)

    frmLevel = Frame(resultsScreen, width=width, height=(height - 60))
    frmLevel.pack(
        side=LEFT, pady=(20, 20), padx=(20, 10), fill=BOTH, expand=TRUE
    )
    frmMeasurement = Frame(resultsScreen, width=width, height=(height - 60))
    frmMeasurement.pack(
        side=LEFT, pady=(20, 20), padx=(10, 20), fill=BOTH, expand=TRUE
    )
    frmScore = Frame(resultsScreen, width=width, height=(height - 60))
    frmScore.pack(
        side=LEFT, pady=(20, 20), padx=(10, 20), fill=BOTH, expand=TRUE
    )

    lblLevel = Label(
        frmLevel, text="— LEVEL —", font=("Montserrat ExtraBold", 20)
    )
    lblLevel.pack(fill=X)
    lblLevel1 = Label(frmLevel, text="Level 1", font=("Montserrat", 20))
    lblLevel1.pack(fill=X)
    lblLevel2 = Label(frmLevel, text="Level 2", font=("Montserrat", 20))
    lblLevel2.pack(fill=X)
    lblLevel3 = Label(frmLevel, text="Level 3", font=("Montserrat", 20))
    lblLevel3.pack(fill=X)
    lblLevel4 = Label(frmLevel, text="Level 4", font=("Montserrat", 20))
    lblLevel4.pack(fill=X)
    lblLevel5 = Label(frmLevel, text="Level 5", font=("Montserrat", 20))
    lblLevel5.pack(fill=X)
    lblLevel6 = Label(frmLevel, text="Level 6", font=("Montserrat", 20))
    lblLevel6.pack(fill=X)
    lblLevel7 = Label(frmLevel, text="Level 7", font=("Montserrat", 20))
    lblLevel7.pack(fill=X)
    lblLevel8 = Label(frmLevel, text="Level 8", font=("Montserrat", 20))
    lblLevel8.pack(fill=X)
    lblLevel9 = Label(frmLevel, text="Level 9", font=("Montserrat", 20))
    lblLevel9.pack(fill=X)
    lblLevel10 = Label(frmLevel, text="Level 10", font=("Montserrat", 20))
    lblLevel10.pack(fill=X)

    lblMeas = Label(
        frmMeasurement,
        text="— MEASUREMENT —",
        font=("Montserrat ExtraBold", 20),
    )
    lblMeas.pack(fill=X)
    lblMeas1 = Label(frmMeasurement, text="20 / 200", font=("Montserrat", 20))
    lblMeas1.pack(fill=X)
    lblMeas2 = Label(frmMeasurement, text="20 / 120", font=("Montserrat", 20))
    lblMeas2.pack(fill=X)
    lblMeas3 = Label(frmMeasurement, text="20 / 80", font=("Montserrat", 20))
    lblMeas3.pack(fill=X)
    lblMeas4 = Label(frmMeasurement, text="20 / 60", font=("Montserrat", 20))
    lblMeas4.pack(fill=X)
    lblMeas5 = Label(frmMeasurement, text="20 / 40", font=("Montserrat", 20))
    lblMeas5.pack(fill=X)
    lblMeas6 = Label(frmMeasurement, text="20 / 30", font=("Montserrat", 20))
    lblMeas6.pack(fill=X)
    lblMeas7 = Label(frmMeasurement, text="20 / 20", font=("Montserrat", 20))
    lblMeas7.pack(fill=X)
    lblMeas8 = Label(frmMeasurement, text="20 / 15", font=("Montserrat", 20))
    lblMeas8.pack(fill=X)
    lblMeas9 = Label(frmMeasurement, text="20 / 13", font=("Montserrat", 20))
    lblMeas9.pack(fill=X)
    lblMeas10 = Label(frmMeasurement, text="20 / 10", font=("Montserrat", 20))
    lblMeas10.pack(fill=X)

    lblScore = Label(
        frmScore, text="— SCORE —", font=("Montserrat ExtraBold", 20)
    )
    lblScore.pack(fill=X)
    lblResult1 = Label(frmScore, text=score1, font=("Montserrat", 20))
    lblResult1.pack(fill=X)
    lblResult2 = Label(frmScore, text=score2, font=("Montserrat", 20))
    lblResult2.pack(fill=X)
    lblResult3 = Label(frmScore, text=score3, font=("Montserrat", 20))
    lblResult3.pack(fill=X)
    lblResult4 = Label(frmScore, text=score4, font=("Montserrat", 20))
    lblResult4.pack(fill=X)
    lblResult5 = Label(frmScore, text=score5, font=("Montserrat", 20))
    lblResult5.pack(fill=X)
    lblResult6 = Label(frmScore, text=score6, font=("Montserrat", 20))
    lblResult6.pack(fill=X)
    lblResult7 = Label(frmScore, text=score7, font=("Montserrat", 20))
    lblResult7.pack(fill=X)
    lblResult8 = Label(frmScore, text=score8, font=("Montserrat", 20))
    lblResult8.pack(fill=X)
    lblResult9 = Label(frmScore, text=score9, font=("Montserrat", 20))
    lblResult9.pack(fill=X)
    lblResult10 = Label(frmScore, text=score10, font=("Montserrat", 20))
    lblResult10.pack(fill=X)

    lblGuide = Label(
        frmBottom, text="Patient's Name: ", font=("Montserrat SemiBold", 12)
    )
    lblGuide.pack(side=LEFT, fill=X, padx=(400, 0))
    entName = ttk.Entry(
        frmBottom,
        font=("Montserrat", 12),
        validate="key",
        validatecommand=hasContent,
    )
    entName.pack(side=LEFT, fill=X)
    btnFinish = ttk.Button(
        frmBottom, text="Finish", state="disabled", command=lambda: startOver()
    )
    btnFinish.pack(side=LEFT, padx=10, pady=10, ipadx=30, ipady=10)


######################

######################
def hasContent():
    isFilled = entName.get()
    # Enable/disable the button based on the contents of the entry widget
    if isFilled:
        btnFinish.config(state="normal")
        return True
    else:
        btnFinish.config(state="disabled")
        return True


######################

######################
def screenshot():
    x = resultsScreen.winfo_rootx()
    y = resultsScreen.winfo_rooty()
    w = resultsScreen.winfo_width()
    h = resultsScreen.winfo_height()

    filename = entName.get()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join(
        os.path.join(os.environ["USERPROFILE"]), "Desktop", "Assessments"
    )
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    full_filename = rf"{folder_path}\{filename}_{today}.png"
    screenshot = ImageGrab.grab(bbox=(x, y, x + w, y + h - 70))
    screenshot.save(full_filename)


######################

######################
def startOver():
    screenshot()
    cap.release()
    cv2.destroyAllWindows()
    resultsScreen.destroy()
    main.destroy()
    os.system("python app.py")


######################

######################
def main():
    # Define self as global variable
    global main

    # Define root frame
    main = Tk()

    main.bind("<Escape>", lambda e: main.quit())

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
        text="VISUAL ACUITY ASSESSMENT DEVICE\n"
        "FOR MUTE AND/OR DEAF-MUTE INDIVIDUALS",
        font=("Montserrat ExtraBold", 35),
    )
    lblTitle.pack(pady=(220, 0), fill=X)
    lblAuthors = Label(
        main,
        text="• Cariaga • Pantallano • Tiu • Villanueva • Yango •",
        font=("Montserrat", 15),
    )
    lblAuthors.pack(pady=(0, 200), fill=X)
    lblGuide = Label(
        main,
        text="Press the [Start] button to start",
        font=("Century Gothic", 10),
    )
    lblGuide.pack(ipady=5, fill=X)
    btnStart = ttk.Button(main, text="Start", command=lambda: levelselect())
    btnStart.pack(ipadx=50, ipady=10)
    btnExit = ttk.Button(main, text="Exit", command=lambda: main.destroy())
    btnExit.pack(ipadx=50, ipady=10)

    # Run the main() function
    main.mainloop()


######################

main()
