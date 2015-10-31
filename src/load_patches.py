import pickle
import random
#import cPickle as pickle
import numpy as np
import cv2

videos = pickle.load(open('data/videos_to_pickle.p','rb'))

print("Total Videos : %i" %len(videos))
num_patches = 10000

def get_patches(videos):

	patch_size = 15
	image_rows = 144
	image_cols = 180

	patches = []
    
	for i in range(num_patches):
		rand_video = int(random.uniform(0,56))
		video = videos[rand_video]
		#print("Video: " + str(rand_video))
		print("Reading : %i" %(i+1))
	
		num_frames  = len(video)
		rand_frame = int(random.uniform(0,num_frames))
		
		x = random.randint(0,image_rows - patch_size)
		y = random.randint(0,image_cols - patch_size)
		
		frame = videos[rand_video][rand_frame]
		#cv2.imwrite('patches/patch_'+str(i+1)+'.png',frame[x:x + patch_size, y:y + patch_size])
		patch = frame[x:x + patch_size, y:y + patch_size].reshape(patch_size * patch_size)
		patches.append(patch)
		
	patches = np.array(patches)
	return patches

patches = get_patches(videos)
pickle.dump(patches,open('data/patches_'+str(num_patches)+'.p','wb'),-1)

print('\nTotal ' + str(num_patches) + ' patches extracted...')

