"""
Script for converting all the training images to a compressed pickle file.

Image directory must be provided from command line.
"""

import sys, os, cv2
import numpy as np
import cPickle as pickle

directory = None

if len(sys.argv)<2:
    print "No directory given."
else:
    directory = sys.argv[1] #directory containing all the training image for RBM

def compressImages(filepath):
    images = [] #container for storing all the images

    for f in os.listdir(filepath):    
        if f.split(".")[-1]=="png":
            link = filepath+str(f)
            if os.path.isfile(link):
                print "Reading image: ",filepath+str(f)
                image = cv2.imread(filepath+str(f),0) #read all the images using opencv
                images.append(image)
    images = np.array(images) # converting the container to a numpy ndarray
    print images.shape
    pickle.dump(images, open('data/image_for_rbm.p','wb'), -1) # compressing the ndarray to a pickle file
    print "Total",len(images),"images compressed."

if directory is not None:
    compressImages(directory)
