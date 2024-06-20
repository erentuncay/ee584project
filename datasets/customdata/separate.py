# This file is used for separating the images in the folders of IRDST dataset for use.
# The rate and number of frames for training and validation can be changed in the separation parts.

import numpy
import random
import os
import shutil

train_dir = "./train/vid"
det_dir = "./train/det"
val_dir = "./val/images"
test_dir = "./test/images"
train_ann = "./annotation/train_vid"
det_ann = "./annotation/train_det"
val_ann = "./annotation/val"
test_ann = "./annotation/test"
os.mkdir("./train/vid")
os.mkdir("./train/det")
os.mkdir("./val/images")
os.mkdir("./test/images")
os.mkdir("./annotation/train_vid")
os.mkdir("./annotation/train_det")
os.mkdir("./annotation/val")
os.mkdir("./annotation/test")

folders = 85
# folders = 317 #simulation frames

for i in range(folders):
    path = "./real/images/"+str(i)
    files = len(os.listdir(path))
    train_set = random.sample(range(files),int(files*0.8))
    det_set = random.sample(train_set,int(files*0.4))
    val_set = [name for name in range(files) if name not in train_set]
    train_set = [name for name in train_set if name not in det_set]
    test_set = random.sample(val_set,int(files*0.1))
    val_set = [name for name in val_set if name not in test_set]
    print("Current folder: "+str(i))
    for k in range(files):
        image_name = "./real/images/"+str(i)+"/1("+str(k+1)+").png"
        annot_name = "./real/boxes/"+str(i)+"/1("+str(k+1)+").txt"
        if k in train_set:
            shutil.copy(image_name,train_dir+"/"+str(i)+"_"+str(k+1)+".png")
            shutil.copy(annot_name,train_ann+"/"+str(i)+"_"+str(k+1)+".txt")
        elif k in det_set:
            shutil.copy(image_name,det_dir+"/"+str(i)+"_"+str(k+1)+".png")
            shutil.copy(annot_name,det_ann+"/"+str(i)+"_"+str(k+1)+".txt")
        elif k in val_set:
            shutil.copy(image_name,val_dir+"/"+str(i)+"_"+str(k+1)+".png")
            shutil.copy(annot_name,val_ann+"/"+str(i)+"_"+str(k+1)+".txt")
        elif k in test_set:
            shutil.copy(image_name,test_dir+"/"+str(i)+"_"+str(k+1)+".png")
            shutil.copy(annot_name,test_ann+"/"+str(i)+"_"+str(k+1)+".txt")