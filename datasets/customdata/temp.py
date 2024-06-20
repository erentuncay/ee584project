""" import numpy
import random
import os
import shutil

train_dir = "./train/vid"
det_dir = "./train/det"
train_ann = "./annotation/train_vid"
det_ann = "./annotation/train_det"
all_frames = os.listdir(train_dir)
det_frames = random.sample(all_frames,len(all_frames)//2)

for frame in det_frames:
    temp = frame.split('.')[0]
    shutil.move(train_dir+"/"+frame,det_dir+"/"+frame)
    shutil.move(train_ann+"/"+temp+".txt",det_ann+"/"+temp+".txt") """

""" import os
from natsort import natsorted

path = "./val/images"
frames_list = os.listdir(path)
frames_list = natsorted(frames_list)
temp = 0
folder_checker = 0
fldr_temp = 0

for file in frames_list:
    temp += 1
    folder_number = file.split(".")[0].split("_")[0]
    if int(folder_number) == folder_checker:
        os.rename(path+"/"+file, path+"/"+folder_number+"_"+str(fldr_temp)+".png")
        to_add = [folder_number+"_"+str(fldr_temp)+" "+str(temp)+"\n"]
        with open('./ImageSets/val_frames.txt', 'a') as f:
            f.write('\n'.join(to_add))
        fldr_temp +=1
    else:
        folder_checker += 1
        fldr_temp = 0
        os.rename(path+"/"+file, path+"/"+folder_number+"_"+str(fldr_temp)+".png")
        to_add = [folder_number+"_"+str(fldr_temp)+" "+str(temp)+"\n"]
        with open('./ImageSets/val_frames.txt', 'a') as f:
            f.write('\n'.join(to_add))
        fldr_temp = 1 """


""" import os

with open('./ImageSets/old_val_frames.txt', 'r') as f:
    old = f.readlines()
with open('./ImageSets/new_val_frames.txt', 'r') as f:
    new = f.readlines()

for i in range(4103):
    temp_old = old[i].strip().split(" ")
    temp_new = new[i].strip()
    folder = temp_old[0].split("_")[0]
    frame = temp_old[0].split("_")[1]
    last = len(os.listdir("./real/images/"+folder))
    to_add = [temp_new+" "+frame+" "+str(last)+"\n"]
    with open('./ImageSets/val_frames.txt', 'a') as f:
        f.write('\n'.join(to_add)) """



""" import os
from natsort import natsorted
new_list = natsorted(os.listdir("./val/images"))
old_list = natsorted(os.listdir("./annotation/val"))

for i in range(4103):
    os.rename("./annotation/val/"+old_list[i],"./annotation/val/"+new_list[i].split(".")[0]+".txt") """



import os
from natsort import natsorted
import shutil
import cv2
import numpy as np

path = "./real/images/6"
images = os.listdir(path)
images = natsorted(images)

for i in range(len(images)):
    shutil.copy(path+"/"+images[i],"./demo/%06d.png"%i)
    img = cv2.imread("./demo/%06d.png"%i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = np.zeros_like(img)
    img2[:,:,0] = gray
    img2[:,:,1] = gray
    img2[:,:,2] = gray
    cv2.imwrite("./demo/%06d.png"%i, img2)

