from PIL import Image, ImageDraw
import sys

im = Image.open("Two.png")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
im.show()