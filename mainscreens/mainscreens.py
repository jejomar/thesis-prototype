from tkinter import *
from tkinter import ttk

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
def itsChosen(level, eye):
    global chosenlevel
    global choseneye

    chosenlevel = level

    if eye == "left":
        eyeScreen.withdraw()
        lefteyeinstr()
    else:
        eyeScreen.withdraw()
        righteyeinstr()
######################

######################
def levelselect():
    global levselScreen
    global levsel
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
    levselScreen.withdraw()

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

    btnLeft = ttk.Button(frmLeft, text="Left Eye", image = right, command=lambda: itsChosen(level, "left"))
    btnLeft.pack(pady=(30,20), padx=20, ipady=150, ipadx=200)
    lblLeft = Label(frmLeft, text="LEFT EYE", font=("Arial", 20))
    lblLeft.pack()
    btnRight = ttk.Button(frmRight, text="Right Eye", image = left, command=lambda: itsChosen(level, "right"))
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

    btnBegin = ttk.Button(leinstrScreen, text="Begin", command=lambda: returnLEye())
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

    btnBegin = ttk.Button(reinstrScreen, text="Begin", command=lambda: returnREye())
    btnBegin.pack(padx=10, pady=10, ipadx=30, ipady=10, anchor=E)

    reinstrScreen.mainloop()
######################

######################
def main():
    global main

    main = Tk()
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    width = screen_width * 0.7
    height = screen_height * 0.7
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    main.title("Visual Acuity Assessment Device for Mute and/or Mute Individuals")
    main.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main.overrideredirect(0)

    lblTitle = Label(main, text="Visual Acuity Assessment Device for Mute\n"
                     "and or Deaf/Mute Individuals", font=("Arial Black", 40))
    lblTitle.pack(ipady = 250, fill=X)
    lblGuide = Label(main, text="Press the button to start...", font=("Century Gothic", 10))
    lblGuide.pack(ipady = 5, fill=X)
    btnStart = ttk.Button(main, text="Start", command=lambda: levelselect())
    btnStart.pack(ipadx = 50, ipady = 10)

    main.mainloop()
######################

main()
