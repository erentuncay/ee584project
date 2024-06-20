# This file is created to list the frame names in a way that is defined for MEGA implementation
# For proper working, ImageSets and corresponding .txt files should exist empty in the current folder.

import os
from natsort import natsorted

path = "./train/det"
frames_list = os.listdir(path)
frames_list = natsorted(frames_list)
old_path = "real/images"

for file in frames_list:
    splitted_file = file.split("_")
    origin_length = len(os.listdir(old_path+"/"+splitted_file[0]))
    frame_number = splitted_file[1].split(".")[0]
    to_add = [file.split(".")[0]+" "+str(1)+" "+frame_number+" "+str(origin_length)+"\n"]
    with open('./ImageSets/det_frames.txt', 'a') as f:
        f.write('\n'.join(to_add))

""" path = "./val/images"
frames_list = os.listdir(path)
frames_list = natsorted(frames_list)
temp = 0

for file in frames_list:
    temp += 1
    frame_number = file.split(".")[0]
    to_add = [path+"/"+frame_number+" "+str(temp)+"\n"]
    with open('./ImageSets/val_frames.txt', 'a') as f:
        f.write('\n'.join(to_add)) """
