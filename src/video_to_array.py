"""
Reads each video file and stores each frames as an array , and store all the frames in the video list
"""

import numpy as np 
import cv2
import os

filepath = 'data/'

videos = []

for f in os.listdir(filepath):
	if f.split('.')[-1] == 'avi':
		if os.path.isfile(filepath + str(f)):
			cap = cv2.VideoCapture(filepath + str(f))

			frames = []

			while True:
				ret, frame = cap.read()

				if frame is None:
					break

				gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				cv2.imshow('action',gray)
				frames.append(gray)
				cv2.waitKey(10)

			frames = np.array(frames)
			videos.append(frames)
			cap.release()
		
videos = np.array(videos)
			
#print(videos)
#print(len(videos))

cv2.destroyAllWindows()