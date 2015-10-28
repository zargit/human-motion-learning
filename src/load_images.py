import cPickle as pickle
import numpy as np 


def unpickle(filename):
	f = open(filename,'rb')
	images = pickle.load(f)
	f.close()
	return images

