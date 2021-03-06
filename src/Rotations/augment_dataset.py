import sys
import os

import cPickle as pickle
import numpy as np

'''
Give as argv[1] the directory with the data.
Example:
python2 augment_dataset.py /home/ireyes/chunks_feat_50000/chunks_train
'''
def rotate(filename, directory, degrees):
    im_keys = ['temp_images', 'SNR_images', 'diff_images', 'sci_images']
    assert degrees%90==0
    k = degrees/90
    data_dict = np.load(directory+'/'+filename)
    rot_dict = dict()
    for key in data_dict.keys():
        if key in im_keys:
            ims = []
            old_mat = data_dict[key]
            for im in old_mat:
                ims.append(np.rot90(im.reshape(21,21), k=k).flatten())
            rot_dict[key] = np.array(ims)
        else:
            rot_dict[key] = data_dict[key]
    with open(directory+'/'+str(degrees)+'_'+filename, "w") as f:
        pickle.dump(rot_dict, f, pickle.HIGHEST_PROTOCOL)
    
    
if __name__=='__main__':
    train_dir = sys.argv[1]
    files = os.listdir(train_dir)
    files.sort()
    for f in files:
        print f
        rotate(f,train_dir,90)
        rotate(f,train_dir,180)
        rotate(f,train_dir,270)
