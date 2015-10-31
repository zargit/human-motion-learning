import cPickle as pickle
#import pickle 
import numpy as np 

filename = 'data/image_for_rbm.p'

def unpickle(filename):
	f = open(filename,'rb')
	images = pickle.load(f)
	f.close()
	return images

def load_patches(filename):
	patch_size = 12
	num_patches = 500
	image_size = 144
	num_images = 56

	images = unpickle(filename)

	patches = np.zeros(shape=(patch_size*patch_size,num_patches))
	image_data = images['data'][0:2]
	return image_data


print(load_patches(filename))