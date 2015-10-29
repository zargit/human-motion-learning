import numpy as np 
import cv2


cap = cv2.VideoCapture('')

frames = []

while True:

	ret, frame = cap.read()

	if frame is None:
		break

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('walk',gray)

	frames.append(gray)

	cv2.waitKey(10)

frames = np.array(frames)

print(frames)

cap.release()
cv2.destroyAllWindows()