# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

	folder = "E:\\Internship\\Data_Annotation\\17dec-scraped\\png"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"{str(count+421)}.png"
		src =f"{folder}\\{filename}" # foldername/filename, if .py file is outside folder
		dst =f"{folder}\\{dst}"
		
		# os.rename(src, dst)
		print(src, dst)

# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()
