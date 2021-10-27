#
# File        : walk_file_demo.py  
# Created     : 22/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import os

def walk_file_processing():
    for folder_name, sub_folders, file_names in os.walk("C:/Users/james/DevOpsCourse/OOPR"):
        print("Folder: {}".format(folder_name))
        for sub_folder in sub_folders:
            print("Folder name: {0} is a sub-folder in {1}".format(sub_folder, folder_name))

        for file_name in file_names:
            print("{0} is a file inside {1}".format(file_name, folder_name))

        print("\n")

if __name__ == '__main__':
    walk_file_processing()
