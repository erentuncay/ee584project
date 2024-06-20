# This file is created to missing frame number in the folders of datasets

import os
import numpy as np
from natsort import natsorted

falses = np.array([0,8,28,37,47,49,51,55,56,83]) # folders that need correction in frame numbers

for k in falses:
    path1 = "./real/images/"+str(k)
    path2 = "./real/boxes/"+str(k)
    all_list1 = os.listdir(path1)
    all_list1 = natsorted(all_list1)
    all_list2 = os.listdir(path2)
    all_list2 = natsorted(all_list2)
    length = len(all_list1)
    temp = 1
    for i in range(1,length+1):
        current = "./real/images/"+str(k)+"/1("+str(i)+").png"
        current2 = "./real/boxes/"+str(k)+"/1("+str(i)+").txt"
        if os.path.exists(current):
            continue
        else:
            os.rename(path1+"/"+all_list1[-temp],current)
            os.rename(path2+"/"+all_list2[-temp],current2)
            temp +=1

            