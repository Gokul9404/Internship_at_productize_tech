""""
This file is used to get some random images from the final folder (untracked folder),
and paste it on the '../Equipment/Preprocessed' folder.

Such that we can have view of the Processing beig done on the images 
"""
import os
import random
import cv2

path = "I:\\Internship\\Data_Annotation\\Final"
new_path = "I:\\Internship\\Data_Annotation\\F78-Gym_equipment\\Equipment\\Preprocessed"
fldr_lst = os.listdir(path)

count = 1
copied_image_no = 1
for folder in fldr_lst:
    fldr_path = os.path.join(path, folder)
    images_path = os.listdir(fldr_path)
    image_lst = []
    
    for image in images_path:
        read_path = os.path.join(fldr_path, image)
        count+=1
        image_lst.append(read_path)
    
    Equipment_type = "_".join(folder.split(" ")[1:])
    final_images  = random.choices(image_lst, k=2)
    # print(final_images,Equipment_type)
    
    for image in final_images:
        img = f"image_{copied_image_no}-{Equipment_type}.png"
        write_path = os.path.join(new_path, img)
        copied_image_no+=1
        Img = cv2.imread(image)
        print(f"{image} -> {img} - {write_path}")
        cv2.imwrite(write_path, Img)

print(f"{count} {copied_image_no}")