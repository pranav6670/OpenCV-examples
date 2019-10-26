import cv2

img = cv2.imread('test1.jpeg')

print("The properties of the image are:")
print("Shape:" + str(img.shape))
print("Total no. of pixels:" + str(img.size))
print("Data type of image:" + str(img.dtype))

