import cv2
import numpy as np
import os

path = 'data/raw_data/'				#path of the raw_data
path2 = 'data/training_data/'		#path to store compressed data

def compressVideo(path,path2):
	#list of all the folders that contain respected video sequences
	folder = [path + f +str('/') for f in os.listdir(path) if not f.startswith('.')]

	#for each folder get the video files 
	for fol in folder:
		
		i = 1			#initialize the label for first image

		#newpath = path2
		#list of all the files in that folder
		files = [fol + f for f in os.listdir(fol) if not f.startswith('.')]
		
		#for each video file in the files list
		for file_in in files:
			#get the video file	
			cam = cv2.VideoCapture(file_in)

			firstframe = None 				#initialize the first frame 
			#create a numpy array for the final image of all the video frames
			finalImage = np.zeros((144,180), dtype=np.uint8)	

			#keep reading the frames from the video
			while True:
				ret, img = cam.read()
				
				# no frame is read		
				if img is None:
					break
				# convert th color frame to grayscale
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
				#initialize the firstframe to the captured frame	
				if firstframe is None:
					firstframe = np.copy(gray)

				# calculate the difference between the first frame and the next frame	
				framedelta = cv2.absdiff(firstframe,gray)
				
				#calculate the threshold to convert the frame to the binary
				thresh = cv2.threshold(framedelta, 50, 255, cv2.THRESH_BINARY)[1]
		 	
				thresh = cv2.dilate(thresh, None, iterations=2)
				
				# add all the frames 	
				finalImage += thresh
				
				#set the first frame to the next frame in the video sequence
				firstframe = np.copy(gray)
		
				if(cv2.waitKey(10) == 27):
					break
			
			filename = fol[14:-1]	#get the action name of the video to label the image
			
			#newpath  = path2  

			# save the image of all the video frames cropped together
			cv2.imwrite(path2 + (str(filename) +'_'+ str(i)+'.png'), finalImage)
			
			i+=1 #increment the counter

		cam.release()	#done reading video	
