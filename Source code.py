import os
import shutil
from tkinter import filedialog

# Obtain the path to be organized
file_path = filedialog.askdirectory()

# Create a dictionary to store file types and their corresponding folders
filetype_dict = {}

# Iterate over all files in the directory
for file in os.listdir(file_path):
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(file_path, file)):
        # Get the file type (extension)
        filetype = file.split('.')[-1]
        
        # Create a new folder for the file type if it doesn't exist
        new_folder_name = os.path.join(file_path, f"{filetype}_files")
        if not os.path.isdir(new_folder_name):
            os.mkdir(new_folder_name)
        
        # Move the file to its corresponding folder
        src_path = os.path.join(file_path, file)
        dest_path = new_folder_name
        shutil.move(src_path, dest_path)
        print(f"{src_path} >> {dest_path}")
