# This file is created to resize the images to a fixed size since the IRDST dataset include
# some frames in different sizes from the others.

import os
import cv2

path = "./train/vid"
#path = "./train/det"
#path = "./val/images"
#path = "./test/images"

all_images = os.listdir(path)

for image in all_images:
    img_folder = image.split("_")[0]
    if img_folder in ['1','2','3','61','62','63','64']:
        img = path+"/"+image
        image2resize = cv2.imread(img)
        resized_image = cv2.resize(image2resize,(704,512), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(img,resized_image)
    else:
        continue