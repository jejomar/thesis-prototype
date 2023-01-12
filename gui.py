import random
import string
import sys
from tkinter import *

global eyeResult


def getRan(count):
    setLet = random.sample(string.ascii_uppercase, count)
    return setLet


def scrtitle():
    global scrtitle

    scrtitle = Tk()
    scrtitle.title(
        "Visual Acuity Assessment Device for Mute and/or Deaf-Mute Individuals"
    )
    scrtitle.state("zoomed")

    screen_width = scrtitle.winfo_screenwidth()
    screen_height = scrtitle.winfo_screenheight()
    print(screen_width, screen_height)
    scrtitle.geometry("%dx%d+0+0" % (screen_width, screen_height))
    scrtitle.overrideredirect(0)

    lbltitle = Label(
        scrtitle,
        text="Visual Acuity Assessment Device"
        "\n for Mute and/or Deaf/Mute Individuals",
        font=("Arial Black", 30),
        fg="black",
    )
    lbltitle.pack(pady=25)
    btnstart = Button(scrtitle, text="Start", command=lambda: scrlevsel())
    btnstart.pack(pady=25)

    scrtitle.mainloop()


def scrlevsel():
    scrtitle.destroy()
    global scrlevsel

    scrlevsel = Tk()
    scrlevsel.title("Level Select")
    scrlevsel.state("zoomed")

    screen_width = scrlevsel.winfo_screenwidth()
    screen_height = scrlevsel.winfo_screenheight()
    print(screen_width, screen_height)
    scrlevsel.geometry("%dx%d+0+0" % (screen_width, screen_height))
    scrlevsel.overrideredirect(0)

    lvllevsel = Label(
        scrlevsel, text="Level Select", font=("Arial Black", 50), fg="black"
    )
    lvllevsel.pack(pady=25)
    btnlevone = Button(
        scrlevsel, text="Level 1", command=lambda: screyesel("one")
    )
    btnlevone.pack(pady=10)
    btnlevtwo = Button(
        scrlevsel, text="Level 2", command=lambda: screyesel("two")
    )
    btnlevtwo.pack(pady=10)
    btnlevthr = Button(
        scrlevsel, text="Level 3", command=lambda: screyesel("thr")
    )
    btnlevthr.pack(pady=10)
    btnlevfou = Button(
        scrlevsel, text="Level 4", command=lambda: screyesel("fou")
    )
    btnlevfou.pack(pady=10)
    btnlevfiv = Button(
        scrlevsel, text="Level 5", command=lambda: screyesel("fiv")
    )
    btnlevfiv.pack(pady=10)
    btnlevsix = Button(
        scrlevsel, text="Level 6", command=lambda: screyesel("six")
    )
    btnlevsix.pack(pady=10)
    btnlevsev = Button(
        scrlevsel, text="Level 7", command=lambda: screyesel("sev")
    )
    btnlevsev.pack(pady=10)
    btnleveig = Button(
        scrlevsel, text="Level 8", command=lambda: screyesel("eig")
    )
    btnleveig.pack(pady=10)
    btnlevnin = Button(
        scrlevsel, text="Level 9", command=lambda: screyesel("nin")
    )
    btnlevnin.pack(pady=10)
    btnlevten = Button(
        scrlevsel, text="Level 10", command=lambda: screyesel("ten")
    )
    btnlevten.pack(pady=10)

    scrlevsel.mainloop()


def screyesel(levsel):
    scrlevsel.destroy()
    global screyesel
    global levSelected

    levSelected = levsel

    screyesel = Tk()
    screyesel.title("Level Select")
    screyesel.state("zoomed")

    screen_width = screyesel.winfo_screenwidth()
    screen_height = screyesel.winfo_screenheight()
    print(screen_width, screen_height)
    screyesel.geometry("%dx%d+0+0" % (screen_width, screen_height))
    screyesel.overrideredirect(0)

    lbleyesel = Label(
        screyesel, text="Eye", font=("Arial Black", 50), fg="black"
    )
    lbleyesel.pack(pady=25)
    btnlefeye = Button(screyesel, text="Left Eye", command=lambda: scrlefins())
    btnlefeye.pack(pady=25)
    btnrgheye = Button(
        screyesel, text="Right Eye", command=lambda: scrrghins()
    )
    btnrgheye.pack(pady=25)

    """
    elif levsel == "thr":
        levSelected = scrlevthr
    elif levsel == "for":
        levSelected = scrlevfou()
    elif levsel == "fiv":
        levSelected = scrlevfiv()
    elif levsel == "six":
        levSelected = scrlevsix()
    elif levsel == "sev":
        levSelected = scrlevsev()
    elif levsel == "eig":
        levSelected = scrleveig()
    elif levsel == "nin":
        levSelected = scrlevnin()
    else:
        levSelected = scrlevten()
    """
    screyesel.mainloop()


def scrlefins():
    screyesel.destroy()
    global scrlefins
    global eyeSelected

    eyeSelected = "left"

    scrlefins = Tk()
    scrlefins.title("Instructions [L]")
    scrlefins.state("zoomed")

    screen_width = scrlefins.winfo_screenwidth()
    screen_height = scrlefins.winfo_screenheight()
    print(screen_width, screen_height)
    scrlefins.geometry("%dx%d+0+0" % (screen_width, screen_height))
    scrlefins.overrideredirect(0)

    lbllefins = Label(
        scrlefins,
        text="Instructions [L]",
        font=("Arial Black", 50),
        fg="black",
    )
    lbllefins.pack(pady=25)
    btnbegex = Button(
        scrlefins,
        text="Begin Exam",
        command=lambda: selected(eyeSelected, levSelected),
    )
    btnbegex.pack(pady=25)

    scrlefins.mainloop()


def scrrghins():
    screyesel.destroy()
    global scrrghins
    global eyeSelected

    eyeSelected = "right"

    scrrghins = Tk()
    scrrghins.title("Instructions [R]")
    scrrghins.state("zoomed")

    screen_width = scrrghins.winfo_screenwidth()
    screen_height = scrrghins.winfo_screenheight()
    print(screen_width, screen_height)
    scrrghins.geometry("%dx%d+0+0" % (screen_width, screen_height))
    scrrghins.overrideredirect(0)

    lblrghins = Label(
        scrrghins,
        text="Instructions [R]",
        font=("Arial Black", 50),
        fg="black",
    )
    lblrghins.pack(pady=25)
    btnbegex = Button(
        scrrghins,
        text="Begin Exam",
        command=lambda: selected(eyeSelected, levSelected),
    )
    btnbegex.pack(pady=25)

    scrrghins.mainloop()


def selected(ins, lev):
    if ins == "left":
        if lev == "one":
            scrlefins.destroy()
            scrlevone()
        elif lev == "two":
            scrlefins.destroy()
            scrlevtwo()
    else:
        if lev == "one":
            scrrghins.destroy()
            scrlevone()
        elif lev == "two":
            scrrghins.destroy()
            scrlevtwo()


def scrlevone():
    global visMeasure
    global scrlevone

    visMeasure = "20/200"

    rone = getRan(1)
    print(rone)

    scrlevone = Tk()
    scrlevone.title("Level 1")
    scrlevone.state("zoomed")

    screen_width = scrlevone.winfo_screenwidth()
    screen_height = scrlevone.winfo_screenheight()
    print(screen_width, screen_height)
    scrlevone.geometry("%dx%d+0+0" % (screen_width, screen_height))

    Frame(scrlevone, width=1536, height=864, bg="#000000").place(x=0, y=0)

    for ind in range(len(rone)):
        label2 = Label(
            scrlevone,
            text=rone[ind],
            font=("Arial Black", 50),
            fg="white",
            bg="black",
        )
        label2.pack(side=LEFT, fill=X, padx=220)
        # label2.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Samples only for screen flow.
    btnsuccess = Button(
        scrlevone,
        text="Success",
        command=lambda: [scrlevone.destroy(), scrlevtwo()],
    )
    btnsuccess.pack(pady=25)
    btnresult = Button(
        scrlevone, text="Failed", command=lambda: scrresult("one", "20/200")
    )
    btnresult.pack(pady=25)

    scrlevone.mainloop()


def scrlevtwo():
    global scrlevtwo
    global visMeasure

    visMeasure = "20/100"

    rtwo = getRan(2)
    print(rtwo)

    scrlevtwo = Tk()
    scrlevtwo.title("Level 2")
    scrlevtwo.state("zoomed")

    screen_width = scrlevtwo.winfo_screenwidth()
    screen_height = scrlevtwo.winfo_screenheight()
    print(screen_width, screen_height)
    scrlevtwo.geometry("%dx%d+0+0" % (screen_width, screen_height))

    Frame(scrlevtwo, width=1536, height=864, bg="#000000").place(x=0, y=0)

    for ind in range(len(rtwo)):
        label2 = Label(
            scrlevtwo,
            text=rtwo[ind],
            font=("Arial Black", 50),
            fg="white",
            bg="black",
        )
        label2.pack(side=LEFT, fill=X, padx=220)
        # label2.place(relx=0.5, rely=0.5, anchor=CENTER)

    btnsuccess = Button(
        scrlevtwo, text="Success", command=lambda: scrresult("two", "20/100")
    )
    btnsuccess.pack(pady=25)
    btnresult = Button(
        scrlevtwo, text="Failed", command=lambda: scrresult("two", "20/100")
    )
    btnresult.pack(pady=25)

    scrlevtwo.mainloop()


def scrresult(curr, visMeasure):

    if curr == "one":
        scrlevone.destroy()
    else:
        scrlevtwo.destroy()

    scrresult = Tk()
    scrresult.title("Results Screen")
    scrresult.state("zoomed")

    screen_width = scrresult.winfo_screenwidth()
    screen_height = scrresult.winfo_screenheight()
    print(screen_width, screen_height)
    scrresult.geometry("%dx%d+0+0" % (screen_width, screen_height))
    scrresult.overrideredirect(0)

    lblresult = Label(
        scrresult, text="Results:", font=("Arial Black", 30), fg="black"
    )
    lblresult.pack(pady=25)
    lblvismea = Label(
        scrresult, text=visMeasure, font=("Arial Black", 75), fg="black"
    )
    lblvismea.pack(pady=25)
    btnfinish = Button(scrresult, text="Finish", command=lambda: sys.exit())
    btnfinish.pack(pady=50)

    scrresult.mainloop()


scrtitle()
