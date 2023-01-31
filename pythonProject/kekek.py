from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk

class Test:
    def __init__(self, parent):
        self.parent = parent
        self.b1="up"
        self.xold=None
        self.yold=None
        self.liste=[]
        self.maclasse = MaClasse(self.parent)
    def test(self):
        self.drawingArea=Canvas(self.parent)
        self.drawingArea.pack()
        self.drawingArea.bind("<Motion>",self.motion)
        self.drawingArea.bind("<ButtonPress-1>",self.b1down)
        self.drawingArea.bind("<ButtonRelease-1>",self.b1up)
    def b1down(self,event):
        self.b1="down"
    def b1up(self,event):
        self.b1="up"
        self.xold=None
        self.yold=None
        self.liste.append((self.xold,self.yold))
    def motion(self,event):
        if self.b1=="down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,fill="red",width=3,smooth=TRUE)
                self.maclasse.dessiner_ligne(self.xold,self.yold,event.x,event.y)
            self.xold=event.x
            self.yold=event.y
            self.liste.append((self.xold,self.yold))

class MaClasse:
    def __init__(self, parent):
        self.s=600,600,3
        self.ma=np.zeros(self.s,dtype=np.uint8)
        self.top = Toplevel(parent)
        self.top.wm_title("OpenCV Image")
        self.label = Label(self.top)
        self.label.pack()
        self.show_image()

    def dessiner_ligne(self, xold, yold, x, y):
        cv2.line(self.ma,(xold, yold),(x,y),[255,255,255],2)
        self.show_image()

    def show_image(self):
        self.im = Image.fromarray(self.ma)
        self.imgtk = ImageTk.PhotoImage(image=self.im)
        self.label.config(image=self.imgtk)


if __name__=="__main__":
    root = Tk()
    root.wm_title("Test")
    v = Test(root)
    v.test()
    root.mainloop()