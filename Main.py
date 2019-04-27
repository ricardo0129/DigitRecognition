from tkinter import *
from time import *
import time

class Window:
    def __init__(self):
        self.m=Tk()
        self.w=Canvas(self.m,width=400,height=400)

    def update(self):
        self.m.update()
        self.m.update_idletasks()
    def callback(self,event):
        startx=event.x
        starty=event.y
        self.w.create_oval(startx-4,starty-4,startx+4,starty+4,fill='black')

    def line(self):
        self.w.pack()
        self.w.bind("<Button1-Motion>", self.callback)


screen = Window()
start=time.time()
fps=0
while True:
    fps+=1
    if (time.time()-start>=1):
        print(fps)
        fps=0
        start=time.time()
    screen.line()
    screen.update()
