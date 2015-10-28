#import cPickle as pickle
import pickle 
import numpy as np 

filename = 'data/image_for_rbm.p'

def unpickle(filename):
	f = open(filename,'rb')
	images = pickle.load(f)
	f.close()
	return images
"""
def loadSequentialPatches(filename):
	patch_size = 12
	num_patches = 500
	image_size = 144

	images = unpickle(filename)

	patches = np.zeros(shape=(patch_size*patch_size,num_patches))

	for i in range(num_patches):
"""


