
from tkinter import *
from PIL import Image, ImageDraw
from Logic import *
import numpy as np
import time


class Window:
    def __init__(self):
        self.m = Tk()
        self.w = Canvas(self.m, width=400, height=400)

        self.image = Image.new("RGB", (400, 400), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle([0,0,400,400],(0,0,0))

        self.start=time.time()

    def update(self):
        self.m.update()
        self.m.update_idletasks()

        if(time.time()-self.start>5.5):
            self.saveImage()
            self.clear()
            self.start=time.time()

    def callback(self, event):
        startx = event.x
        starty = event.y
        self.w.create_oval(startx - 14, starty - 14, startx + 14, starty + 14, fill='black')
        self.draw.ellipse([startx - 14, starty - 14, startx + 14, starty + 14],(255,255,255))


    def clear(self):
        self.image = Image.new("RGB", (400, 400), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle([0, 0, 400, 400], (0, 0, 0))
        self.w.delete("all")

    def saveImage(self):
        self.image = self.image.resize((28, 28), Image.ANTIALIAS)
        aaa=predictImage(self.image)
        bbb=model.predict(aaa)
        print(np.argmax(bbb))

    def line(self):
        self.w.pack()
        self.w.bind("<Button1-Motion>", self.callback)



screen = Window()
start = time.time()
fps = 0

while True:
    fps += 1
    if (time.time() - start >= 1):
        fps = 0
        start = time.time()
    screen.line()
    screen.update()