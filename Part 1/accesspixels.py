import cv2
import numpy as np

m =  cv2.imread("test1.jpeg")

height,width,depth = np.shape(m)

y = 1 # y coordinate(across height)
x = 1 # x coordinate(across width)

print("Value at (1, 1, 0) = " + str(m[y][x][0])) # This will print the pixel value at given coordinates at depth zero(blue)
print("Value at (1, 1, 1) = " + str(m[y][x][1])) # This will print the pixel value at given coordinates at depth one(green)
print("Value at (1, 1, 2) = " + str(m[y][x][2])) # This will print the pixel value at given coordinates at depth two(red)
