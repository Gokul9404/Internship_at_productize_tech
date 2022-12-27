import os

def main():
    # Script to delete images form sub-folder
    folder = "E:\\Internship\\Data_Annotation\\12-dec-vedio\\vedios"
    list_dir = (os.listdir(folder))
    folder_lst = [i for i in list_dir if i.split(".")[-1] != "mov"]
    # print(folder_lst)
    for folders in folder_lst:
        dst = f"{folder}\\{folders}"
        for count, filename in enumerate(os.listdir(dst)):
            src = f"{dst}\{filename}"
            print(count, end=" ")
            if(count % 2 == 0):
                # os.remove(src)
                print(src)
            else:
                print()

# def main():
#     # Script to delete images form a folder
#     dst = "E:\\Internship\\Data_Annotation\\Vedio_generated_images\\vedios\\ved_1 frame"
#     print(dst)
#     x = 0
#     for count, filename in enumerate(os.listdir(dst)):
#         src = f"{dst}\{filename}"
#         print(count, end=" ")
#         if(count % 3 == 0):
#             os.remove(src)
#             print(src)
#             x+=1
#         else:
#             print()
#     print(x)

if __name__ == '__main__':
    main()
