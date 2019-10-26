import cv2
import numpy as np

m =  cv2.imread("test1.jpeg")

height, width, depth= np.shape(m)

# iterate over the entire image.
for y in range(0,height):
    for x in range(0,width):
        print(m[y][x][0])
