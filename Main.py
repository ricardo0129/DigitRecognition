


'''
width = 400
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)

root = Tk()

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
cv.create_line([0, center, width, center], fill='green')

# do the PIL image/draw (in memory) drawings
draw.line([0, center, width, center], green)
    
# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
filename = "my_drawing.jpg"
image1.save(filename)

root.mainloop()

'''

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

        if(time.time()-self.start>4):
            self.saveImage()
            self.clear()
            self.start=time.time()

    def callback(self, event):
        startx = event.x
        starty = event.y
        self.w.create_oval(startx - 8, starty - 8, startx + 8, starty + 8, fill='black')
        self.draw.ellipse([startx - 8, starty - 8, startx + 8, starty + 8],(255,255,255))


    def clear(self):
        self.image = Image.new("RGB", (400, 400), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle([0, 0, 400, 400], (0, 0, 0))
        self.w.delete("all")

    def saveImage(self):
        self.image = self.image.resize((28, 28), Image.ANTIALIAS)
        self.image.show()
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