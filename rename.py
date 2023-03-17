import os
import cv2
import time

path = "I:\\Internship\\Data_Annotation\\New folder"
new_path = "I:\\Internship\\Data_Annotation\\Final"

fldr_lst = os.listdir(path)
fldr_lst = [x for x in fldr_lst if x.split(".")[-1] != 'xlsx']

for folder in fldr_lst:
    fldr_path = os.path.join(path, folder)
    new_fldr_path = os.path.join(new_path, folder)
    images_path = os.listdir(fldr_path)
    image_no = 1
    os.mkdir(new_fldr_path)
    for image in images_path:
        # cv2.imread()
        # cv2.imwrite(f"{Video_folder}\{dst} frame\\Img_{x}.jpg", frame)
        read_path = os.path.join(fldr_path, image)
        
        img = f"image_{image_no}.png"
        image_no+=1
        write_path = os.path.join(new_fldr_path, img)
        Img = cv2.imread(read_path)
        
        print(read_path,write_path)

        cv2.imwrite(write_path, Img)