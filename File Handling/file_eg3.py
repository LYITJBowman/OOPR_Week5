#
# File        : file_eg3.py  
# Created     : 21/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import os


def file_processing3(file_name):
    '''

    :param file_name:
    :return:
    '''

    file_obj = open(file_name, "r+")
    #file_obj.seek(0)
    #file_obj.seek(10,0)
    #file_obj.seek(1, os.SEEK_SET)
    #file_obj.seek(0, os.SEEK_CUR)
    file_obj.seek(0, os.SEEK_END)

    all_file_contents = file_obj.read()
    print(all_file_contents)

    file_obj.close()

if __name__ == '__main__':
    file_processing3("sample.txt")
