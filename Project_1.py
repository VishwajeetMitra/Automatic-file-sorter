# Import the libraries

from tkinter import filedialog
from os import listdir
from os.path import isfile, join
import os
import shutil

# Obtain the path to be organized

file_path = filedialog.askdirectory()

# Obtain all the files from the path in list

files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

# Create the blank list and dictionary

filetype_dict = {}



# Create a loop

for file in files:

	# Split the name of file from dot

	filetype = file.split('.')[-1]
	
	# Give naming to the newly created folders
	
	new_folder_name = file_path+'/' + filetype + '_files'

	# Add the new folder name in dictionary with the key value pairs

	filetype_dict[str(filetype)] = str(new_folder_name)

	# Check if the folder exists or not

	if os.path.isdir(new_folder_name) == True:

	# Come out of the loop if folder exists

		continue
	else:

	# Create the new folder if does not exist

		os.mkdir(new_folder_name)


# Create the loop for all the files

for file in files:

	# Get the source path of each file

	src_path = file_path+'/'+file

	# Split the name of file by dot

	filetype = file.split('.')[-1]

	# Check if the file type exists in the dictionary

	if filetype in filetype_dict.keys():

		# Add the file type in dictionary if not already there

		dest_path = filetype_dict[str(filetype)]

		# Move the file from source path to destination path

		shutil.move(src_path, dest_path)

	print('.',src_path + '>>>' + dest_path)
