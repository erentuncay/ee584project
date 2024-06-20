# This file is used for conversion of 1-channel images to 3-channel

import cv2
import numpy as np
import os

path_list = ["./test/images/", "./val/images/", "./train/det/", "./train/vid/"]

for path in path_list:
    image_list = os.listdir(path)
    for image in image_list:
        img = cv2.imread(path+image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = np.zeros_like(img)
        img2[:,:,0] = gray
        img2[:,:,1] = gray
        img2[:,:,2] = gray
        cv2.imwrite(path+image, img2)