#
# File        : Question1.py  
# Created     : 22/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import os


def practice_q(user_dir):
    total_size = 0
    for file_name in os.listdir(user_dir):
        print(f"{file_name}")
        size = os.path.getsize(os.path.join(user_dir, file_name))
        total_size = total_size + size
    print("The total size of the contents of this directory is: {}".format(total_size))

if __name__ == '__main__':
    user_dir = input("Please enter a directory name: ")
    practice_q(user_dir)
