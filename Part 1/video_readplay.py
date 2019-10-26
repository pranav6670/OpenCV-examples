import cv2

cap = cv2.VideoCapture('../somemovie.mp4') # Replace with your movie

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(480,270))
        cv2.imshow('frame',frame)
    else:
    	break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
