from PIL import Image
import numpy as np
import os

def append_images(images):
    imgs    = [ Image.open(i) for i in images ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.vstack([i.resize(min_shape) for i in imgs])
    imgs_comb = Image.fromarray( imgs_comb)
    return( imgs_comb )



images = [each for each in os.listdir() if '.jpg' in each]
combo_1 = append_images(images)
combo_1.save(images[0].rsplit('_', 1)[0] + '.jpg')
for each in images:
    os.remove(each)