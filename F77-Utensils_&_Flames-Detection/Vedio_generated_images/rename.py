import os

# Function to rename multiple files in a folder
def main():
    x = 1
    folder = "E:\\Internship\\New folder\\background\\b"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"bimg_{str(count+x)}.jpg"
        src =f"{folder}\\{filename}" # foldername/filename, if .py file is outside folder
        dst =f"{folder}\\{dst}"
        print(src, dst)
        os.rename(src, dst)
    print()

# def main2():
#     """Function to rename text files"""
#     x = 2413
#     folder = "E:\\Internship\\Data_Annotation\\Vedio_generated_images\\vedios\\new\\labels"
#     list_dir = (os.listdir(folder))
#     folder_lst = [i for i in list_dir if i.split(".")[-1] == "txt"]
#     print(folder_lst)
#     for count, filename in enumerate(os.listdir(folder)):
#         dst = f"img_{str(count+x)}.txt"
#         src =f"{folder}\\{filename}" # foldername/filename, if .py file is outside folder
#         dst =f"{folder}\\{dst}"
#         print(src, dst)
#         os.rename(src, dst)

# Function to rename multiple files in sub-folders of a folder
# def main():
#     folder = "E:\\Internship\\New folder\\New folder"
#     list_dir = (os.listdir(folder))
#     folder_lst = [i for i in list_dir if i.split(".")[-1] != "mp4"]
#     x = 294
#     # print(folder_lst)
#     for folders in folder_lst:
#         dst = f"{folder}\\{folders}"
#         print(dst)
#         for count, filename in enumerate(os.listdir(dst)):
#             rnm = f"Img_{str(x)}.jpg"
#             x+=1
#             src = f"{dst}//{filename}"
#             st =f"{dst}//{rnm}"
#             os.rename(src, st)
#             # print(src, st)
#     print(x)
            

if __name__ == '__main__':
	main()