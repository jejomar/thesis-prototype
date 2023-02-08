import datetime
import pickle
import random
import string
import threading
import time
from threading import Timer
from tkinter import *
from tkinter import ttk

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk

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
CUE_FONT = ("Courier", 50)

# Global functions
# def timeout():
#     start = datetime.now()

#     if datetime.timedelta.seconds(time.time()) and datetime.timedelta.seconds(start) is 5:

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
######################

######################
def eyeChosen(eye):
    global chosenEye

    chosenEye = eye

    if eye == "left":
        eyeScreen.withdraw()
        lefteyeinstr()
    else:
        eyeScreen.withdraw()
        righteyeinstr()
######################

######################
def lvlChosen():
    if chosenEye == "left":
        if chosenLvl == "one":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_one();
        elif chosenLvl == "two":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_two();
        elif chosenLvl == "thr":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_three();
        elif chosenLvl == "fou":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_four();
        elif chosenLvl == "fiv":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_five();
        elif chosenLvl == "six":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_six();
        elif chosenLvl == "sev":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_seven();
        elif chosenLvl == "eig":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_eight();
        elif chosenLvl == "nin":
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_nine();
        else:
            leinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_ten();
    else:
        if chosenLvl == "one":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_one();
        elif chosenLvl == "two":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_two();
        elif chosenLvl == "thr":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_three();
        elif chosenLvl == "fou":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_four();
        elif chosenLvl == "fiv":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_five();
        elif chosenLvl == "six":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_six();
        elif chosenLvl == "sev":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_seven();
        elif chosenLvl == "eig":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_eight();
        elif chosenLvl == "nin":
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_nine();
        else:
            reinstrScreen.destroy()
            eyeScreen.destroy()
            levselScreen.destroy()
            level_ten();
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

    levselScreen.title("Visual Acuity Assessment Device for Mute and/or Mute Individuals")
    levselScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    levselScreen.overrideredirect(0)
    levselScreen.pack_propagate(0)

    btnReturn = ttk.Button(levselScreen, text="Return", command=lambda: returnTitle())
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady = 10, anchor=W)
    lblTitle = Label(levselScreen, text="LEVEL SELECT", font=("Arial Black", 40))
    lblTitle.pack(fill=X)

    frmTop = Frame(levselScreen, width=width, height=(height-45))
    frmTop.pack(fill = X, pady = (30,25))
    frmBot = Frame(levselScreen, width=width, height=(height-45))
    frmBot.pack(fill = X, pady = (25,50))

    btnLevel1 = ttk.Button(frmTop, text="Level 1", command=lambda: eyetest("one"))
    btnLevel1.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel2 = ttk.Button(frmTop, text="Level 2", command=lambda: eyetest("two"))
    btnLevel2.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel3 = ttk.Button(frmTop, text="Level 3", command=lambda: eyetest("thr"))
    btnLevel3.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel4 = ttk.Button(frmTop, text="Level 4", command=lambda: eyetest("fou"))
    btnLevel4.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel5 = ttk.Button(frmTop, text="Level 5", command=lambda: eyetest("fiv"))
    btnLevel5.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel6 = ttk.Button(frmBot, text="Level 6", command=lambda: eyetest("six"))
    btnLevel6.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel7 = ttk.Button(frmBot, text="Level 7", command=lambda: eyetest("sev"))
    btnLevel7.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel8 = ttk.Button(frmBot, text="Level 8", command=lambda: eyetest("eig"))
    btnLevel8.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel9 = ttk.Button(frmBot, text="Level 9", command=lambda: eyetest("nin"))
    btnLevel9.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)
    btnLevel10 = ttk.Button(frmBot, text="Level 10", command=lambda: eyetest("ten"))
    btnLevel10.pack(side=LEFT, padx=30, pady=30, ipadx=67, ipady=70)

    levselScreen.mainloop()
######################

######################
def eyetest(level):
    global eyeScreen
    global chosenLvl
    levselScreen.withdraw()

    chosenLvl = level

    left = PhotoImage(file=r"lefteye.png")
    right = PhotoImage(file=r"righteye.png")

    eyeScreen = Toplevel(main)
    screen_width = eyeScreen.winfo_screenwidth()
    screen_height = eyeScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    eyeScreen.title("Visual Acuity Assessment Device for Mute and/or Mute Individuals")
    eyeScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    eyeScreen.overrideredirect(0)
    eyeScreen.pack_propagate(0)

    btnReturn = ttk.Button(eyeScreen, text="Return", command=lambda: returnLevSel())
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(eyeScreen, text="CHOOSE THE EYE TO TEST", font=("Arial Black", 40))
    lblTitle.pack(fill=X)

    frmLeft = Frame(eyeScreen, width=width, height=(height - 45))
    frmLeft.pack(side=LEFT, pady=(20,20), padx= (20,10), fill=BOTH, expand=TRUE)
    frmRight = Frame(eyeScreen, width=width, height=(height - 45))
    frmRight.pack(side=LEFT, pady=(20,20), padx= (10,20), fill=BOTH, expand=TRUE)

    btnLeft = ttk.Button(frmLeft, text="Left Eye", image = right, command=lambda: eyeChosen("left"))
    btnLeft.pack(pady=(30,20), padx=20, ipady=150, ipadx=200)
    lblLeft = Label(frmLeft, text="LEFT EYE", font=("Arial", 20))
    lblLeft.pack()
    btnRight = ttk.Button(frmRight, text="Right Eye", image = left, command=lambda: eyeChosen("right"))
    btnRight.pack(pady=(30,20), padx=20, ipady=150, ipadx=200)
    lblRight = Label(frmRight, text="RIGHT EYE", font=("Arial", 20))
    lblRight.pack()

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

    leinstrScreen.title("Visual Acuity Assessment Device for Mute and/or Mute Individuals")
    leinstrScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    leinstrScreen.overrideredirect(0)
    leinstrScreen.pack_propagate(0)

    btnReturn = ttk.Button(leinstrScreen, text="Return", command=lambda: returnLEye())
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(leinstrScreen, text="INSTRUCTIONS BEFORE THE ASSESSMENT", font=("Arial Black", 40))
    lblTitle.pack(fill=X)

    frmInstruction = Frame(leinstrScreen, width=width, height=(height - 80))
    frmInstruction.pack(fill=BOTH, expand=TRUE)

    lblInstruction = Label(frmInstruction,
                            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque mollis sapien nisi,"
                                 "a mollis turpis ullamcorper non. Duis in egestas nunc. Duis non neque ullamcorper, lacinia purus vitae,"
                                 " condimentum augue. Curabitur massa metus, facilisis ac ipsum vel, mattis vehicula velit. "
                                 "Aenean gravida, odio in imperdiet pharetra, metus nulla eleifend mauris, id cursus neque leo id magna. "
                                 "Praesent pulvinar nunc urna, quis ultrices dui suscipit quis.", font=("Arial", 20),
                            justify=LEFT)
    lblInstruction.bind('<Configure>', lambda e: lblInstruction.config(wraplength=width * 0.95))
    lblInstruction.pack(fill=X, padx=10, pady=20)

    btnBegin = ttk.Button(leinstrScreen, text="Begin", command=lambda: lvlChosen())
    btnBegin.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=E)

    leinstrScreen.mainloop()
######################

######################
def righteyeinstr():
    global reinstrScreen
    reinstrScreen = Toplevel(main)
    screen_width = reinstrScreen.winfo_screenwidth()
    screen_height = reinstrScreen.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    reinstrScreen.title("Visual Acuity Assessment Device for Mute and/or Mute Individuals")
    reinstrScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    reinstrScreen.overrideredirect(0)
    reinstrScreen.pack_propagate(0)

    btnReturn = ttk.Button(reinstrScreen, text="Return", command=lambda: returnREye())
    btnReturn.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=W)
    lblTitle = Label(reinstrScreen, text="INSTRUCTIONS BEFORE THE ASSESSMENT", font=("Arial Black", 40))
    lblTitle.pack(fill=X)

    frmInstruction = Frame(reinstrScreen, width=width, height=(height - 80))
    frmInstruction.pack(fill=BOTH, expand=TRUE)

    lblInstruction = Label(frmInstruction, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque mollis sapien nisi,"
                                                "a mollis turpis ullamcorper non. Duis in egestas nunc. Duis non neque ullamcorper, lacinia purus vitae,"
                                                " condimentum augue. Curabitur massa metus, facilisis ac ipsum vel, mattis vehicula velit. "
                                                "Aenean gravida, odio in imperdiet pharetra, metus nulla eleifend mauris, id cursus neque leo id magna. "
                                                "Praesent pulvinar nunc urna, quis ultrices dui suscipit quis.", font=("Arial", 20), justify=LEFT)
    lblInstruction.bind('<Configure>', lambda e: lblInstruction.config(wraplength=width * 0.95))
    lblInstruction.pack(fill=X, padx=10, pady=20)

    btnBegin = ttk.Button(reinstrScreen, text="Begin", command=lambda: lvlChosen())
    btnBegin.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=E)

    reinstrScreen.mainloop()
######################

######################
#Function for image processing

######################

######################
def level_one():  # Define self as global variable
    global run_level_one
    global ctr_level_one

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_one = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_one.winfo_screenwidth()
    screen_height = run_level_one.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_one.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_one.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_one

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_one, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_one = gen_ran_letters()
        print(random_one)

        # Iterate through the list of random_letters
        for i in range(len(random_one)):
            letters = Label(
                letter_frame, text=random_one[i], font=("Courier", 152, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_one, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
    cue_label.pack(side=LEFT, padx=30, pady=10)

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
        frame=cv2.flip(frame,1)


        data = image_processed(frame)

        # Will only get the detected letter only if hands are present in the frame.
        if (output.multi_hand_landmarks):# Line checks if hands are present in the frame
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
            ctr_level_one = 0
            arrlen = len(random_one)
            for i in range(arrlen):
                if detected_letters1[i] == random_one[i]:
                    ctr_level_one = ctr_level_one + 1

            if ctr_level_one != 0:
                print(str(ctr_level_one) + "/" + str(arrlen))
                cv2.destroyAllWindows()
                level_two()
                run_level_one.destroy()
            else:
                results()

        if len(detected_letters1) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
        else:
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
def level_two():  # Define self as global variable
    global run_level_two
    global ctr_level_two

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_two = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_two.winfo_screenwidth()
    screen_height = run_level_two.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_two.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_two.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_two

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_two, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_two = gen_ran_letters()
        print(random_two)

        # Iterate through the list of random_letters
        for i in range(len(random_two)):
            letters = Label(
                letter_frame, text=random_two[i], font=("Courier", 130, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_two, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_two = 0
            arrlen = len(random_two)
            for i in range(arrlen):
                if detected_letters2[i] == random_two[i]:
                    ctr_level_two = ctr_level_two + 1

            if ctr_level_two != 0:
                print(str(ctr_level_two) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_two.withdraw()
                level_three()
            else:
                results()

        if len(detected_letters2) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)

        else:
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

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_three = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_three.winfo_screenwidth()
    screen_height = run_level_three.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_three.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_three.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_thr

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_three, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_thr = gen_ran_letters()
        print(random_thr)

        # Iterate through the list of random_letters
        for i in range(len(random_thr)):
            letters = Label(
                letter_frame, text=random_thr[i], font=("Courier", 108, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_three, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_three = 0
            arrlen = len(random_thr)
            for i in range(arrlen):
                if detected_letters3[i] == random_thr[i]:
                    ctr_level_three = ctr_level_three + 1

            if ctr_level_three != 0:
                print(str(ctr_level_three) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_three.withdraw()
                level_four()
            else:
                results()

        if len(detected_letters3) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
def level_four():  # Define self as global variable
    global run_level_four
    global ctr_level_four

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_four = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_four.winfo_screenwidth()
    screen_height = run_level_four.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_four.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_four.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_fou

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_four, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_fou = gen_ran_letters()
        print(random_fou)

        # Iterate through the list of random_letters
        for i in range(len(random_fou)):
            letters = Label(
                letter_frame, text=random_fou[i], font=("Courier", 87, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_four, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_four = 0
            arrlen = len(random_fou)
            for i in range(arrlen):
                if detected_letters4[i] == random_fou[i]:
                    ctr_level_four = ctr_level_four + 1

            if ctr_level_four != 0:
                print(str(ctr_level_four) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_four.withdraw()
                level_five()
            else:
                results()

        if len(detected_letters4) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
def level_five():  # Define self as global variable
    global run_level_five
    global ctr_level_five

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)
    # Create a frame for the current level
    run_level_five = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_five.winfo_screenwidth()
    screen_height = run_level_five.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_five.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_five.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_five

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_five, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_five = gen_ran_letters()
        print(random_five)

        # Iterate through the list of random_letters
        for i in range(len(random_five)):
            letters = Label(
                letter_frame, text=random_five[i], font=("Courier", 65, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_five, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_five = 0
            arrlen = len(random_five)
            for i in range(arrlen):
                if detected_letters5[i] == random_five[i]:
                    ctr_level_five = ctr_level_five + 1

            if ctr_level_five != 0:
                print(str(ctr_level_five) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_five.withdraw()
                level_six()
            else:
                results()

        if len(detected_letters5) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
def level_six():  # Define self as global variable
    global run_level_six
    global ctr_level_six

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_six = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_six.winfo_screenwidth()
    screen_height = run_level_six.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_six.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_six.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_six

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_six, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_six = gen_ran_letters()
        print(random_six)

        # Iterate through the list of random_letters
        for i in range(len(random_six)):
            letters = Label(
                letter_frame, text=random_six[i], font=("Courier", 43, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_six, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_six = 0
            arrlen = len(random_six)
            for i in range(arrlen):
                if detected_letters6[i] == random_six[i]:
                    ctr_level_six = ctr_level_six + 1

            if ctr_level_six != 0:
                print(str(ctr_level_six) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_six.withdraw()
                level_seven()
            else:
                results()

        if len(detected_letters6) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
def level_seven():  # Define self as global variable
    global run_level_seven
    global ctr_level_seven

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_seven = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_seven.winfo_screenwidth()
    screen_height = run_level_seven.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_seven.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_seven.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_seven

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_seven, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_seven = gen_ran_letters()
        print(random_seven)

        # Iterate through the list of random_letters
        for i in range(len(random_seven)):
            letters = Label(
                letter_frame, text=random_seven[i], font=("Courier", 33, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_seven, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_seven = 0
            arrlen = len(random_seven)
            for i in range(arrlen):
                if detected_letters7[i] == random_seven[i]:
                    ctr_level_seven = ctr_level_seven + 1

            if ctr_level_seven != 0:
                print(str(ctr_level_seven) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_seven.withdraw()
                level_eight()
            else:
                results()

        if len(detected_letters7) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
def level_eight():  # Define self as global variable
    global run_level_eight
    global ctr_level_eight

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_eight = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_eight.winfo_screenwidth()
    screen_height = run_level_eight.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_eight.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_eight.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_eight

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_eight, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_eight = gen_ran_letters()
        print(random_eight)

        # Iterate through the list of random_letters
        for i in range(len(random_eight)):
            letters = Label(
                letter_frame, text=random_eight[i], font=("Courier", 21, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_eight, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_eight = 0
            arrlen = len(random_eight)
            for i in range(arrlen):
                if detected_letters8[i] == random_eight[i]:
                    ctr_level_eight = ctr_level_eight + 1

            if ctr_level_eight != 0:
                print(str(ctr_level_eight) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_eight.withdraw()
                level_nine()
            else:
                results()

        if len(detected_letters8) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
def level_nine():  # Define self as global variable
    global run_level_nine
    global ctr_level_nine

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_nine = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_nine.winfo_screenwidth()
    screen_height = run_level_nine.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_nine.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_nine.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_nine

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_nine, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_nine = gen_ran_letters()
        print(random_nine)

        # Iterate through the list of random_letters
        for i in range(len(random_nine)):
            letters = Label(
                letter_frame, text=random_nine[i], font=("Courier", 15, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_nine, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_nine = 0
            arrlen = len(random_nine)
            for i in range(arrlen):
                if detected_letters9[i] == random_nine[i]:
                    ctr_level_nine = ctr_level_nine + 1

            if ctr_level_nine != 0:
                print(str(ctr_level_nine) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_nine.withdraw()
                level_ten()
            else:
                results()

        if len(detected_letters9) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
######################

######################
def level_ten():  # Define self as global variable
    global run_level_ten
    global ctr_level_ten

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

    # Create a frame for the current level
    run_level_ten = Toplevel(main)

    # Configure window geometry of the new frame
    screen_width = run_level_ten.winfo_screenwidth()
    screen_height = run_level_ten.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    run_level_ten.geometry("%dx%d+%d+%d" % (width, height, x, y))
    run_level_ten.overrideredirect(0)

    global start_time
    global finish

    # Generate the random letters

    # Print the generated letters on the screen
    def print_letters():
        # Define self as a global variable
        global random_ten

        # Create a frame for the letter generated
        letter_frame = Frame(run_level_ten, width=1920, height=840)
        letter_frame.pack(fill=X, expand=True)

        # Run the generate function and set it to the global list 'random_letters'
        random_ten = gen_ran_letters()
        print(random_ten)

        # Iterate through the list of random_letters
        for i in range(len(random_ten)):
            letters = Label(
                letter_frame, text=random_ten[i], font=("Courier", 9, "bold")
            )

            letters.pack(side=LEFT, expand=True)

    print_letters()

    # Display the camera alongside the generated letters
    camera_frame = Frame(
        run_level_ten, width=camera_width, height=camera_height
    )
    camera_frame.pack(side=BOTTOM, fill=X)

    cue_label = Label(
        camera_frame, text=" ", font=CUE_FONT
    )
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
                (20, 50),
                cv2.FONT_HERSHEY_TRIPLEX,
                2,
                (255, 0, 0),
                2,
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
            ctr_level_ten = 0
            arrlen = len(random_ten)
            for i in range(arrlen):
                if detected_letters10[i] == random_ten[i]:
                    ctr_level_ten = ctr_level_ten + 1

            if ctr_level_ten != 0:
                print(str(ctr_level_ten) + "/" + str(arrlen))
                cap.release()
                cv2.destroyAllWindows()
                run_level_ten.withdraw()
                results()
            else:
                results()

        if len(detected_letters10) < 5:

            if output.multi_hand_landmarks:
                #This will be implemented kasi pag unang letter, 8 seconds ang inaantay bago i-record yung letter.
                #Therefore, one na ang detected_letters ay walang laman or equal to zero (0),
                #Ang countdown nya is set to five lang. Pero, kapag may laman na,
                #Ang countdown will be set to eight kasi may cooldown time tayo na 3 seconds.
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
                    cue_label.config(text="Hold the gesture. " + str(countdown - int((curr - start_time).total_seconds())))
            else:
                cue_label.config(text="No hands detected.")
                start_time = curr
                curr = datetime.datetime.now()
                finish = start_time + datetime.timedelta(seconds=5)
                countdown = 5
        else:
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
def results():  # Define self as global variable
    global resultsScreen
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
        text="Visual Acuity Assessment Device for Mute\n"
        "and or Deaf/Mute Individuals",
        font=("Arial Black", 40),
    )
    lblTitle.pack(ipady=250, fill=X)
    lblGuide = Label(
        main, text="Press the button to start...", font=("Century Gothic", 10)
    )
    lblGuide.pack(ipady=5, fill=X)
    btnStart = ttk.Button(main, text="Start", command=lambda: levelselect())
    btnStart.pack(ipadx=50, ipady=10)

    # Run the main() function
    main.mainloop()
######################

main()
