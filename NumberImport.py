from PIL import Image
import numpy as np



def predictImage(filename):
    img = filename

    img.convert('LA')
    width, height = img.size
    dataArray = []
    for i in range(0, width):
        for j in range(0, height):
            dataArray.append(img.getpixel((j, i))[0])
    numArray = np.array(dataArray)
    numArray = numArray.reshape(1, width, height, 1)

    return numArray