import cv2
import numpy as np

m =  cv2.imread("test1.jpeg")

height, width ,depth = np.shape(m)

for py in range(0, height):
    for px in range(0, width):
        m[py][px][0] = 0

cv2.imshow('matrix', m)
cv2.imwrite('output2.png', m)
cv2.waitKey(0)
cv2.destroyAllWindows()
