""" with open('./ImageSets/val_frames - Kopya.txt', 'r') as f:
    old = f.readlines()

for line in old:
    i1 = line.split(" ")[0]
    i3 = line.split(" ")[2]
    i4 = line.split(" ")[3]

    to_add = [i1+" "+str(1)+" "+i3+" "+i4]
    with open('./ImageSets/val_frames.txt', 'a') as f:
        f.write('\n'.join(to_add)) """



import os
import cv2

path = "./demo/"
all_images = os.listdir(path)

for image in all_images:
    img = path+image
    image2resize = cv2.imread(img)
    resized_image = cv2.resize(image2resize,(704,512), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(img,resized_image)

