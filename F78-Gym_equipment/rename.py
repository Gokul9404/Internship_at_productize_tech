import os
import cv2
import time

path = "I:\\Internship\\Data_Annotation\\New folder"
new_path = "I:\\Internship\\Data_Annotation\\Final"

fldr_lst = os.listdir(path)
fldr_lst = [x for x in fldr_lst if x.split(".")[-1] != 'xlsx']
fldr_lst.remove('New folder')

count = 1
for folder in fldr_lst:
    fldr_path = os.path.join(path, folder)
    new_fldr_path = os.path.join(new_path, folder)
    images_path = os.listdir(fldr_path)
    image_no = 1
    os.mkdir(new_fldr_path)
    for image in images_path:
        read_path = os.path.join(fldr_path, image)
        
        img = f"image_{image_no}.png"
        write_path = os.path.join(new_fldr_path, img)
        Img = cv2.imread(read_path)
        
        image_no+=1
        count+=1
        
        print(read_path,write_path)
        cv2.imwrite(write_path, Img)

print(count)