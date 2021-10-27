#
# File        : file_eg2.py  
# Created     : 21/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def file_processing2(file_name):
    '''

    :param file_name:
    :return:
    '''

    file_obj = open(file_name, "r+")
    for line in file_obj:
        print(line.rstrip())

    file_obj.write("\nThe Stig, L700003, M.Eng Mechanical Engineering")
    file_obj.seek(0)

    print("\nAfter new student added: ")
    all_file_contents = file_obj.read()
    print(all_file_contents)
    file_obj.close()

if __name__ == '__main__':
    file_processing2("sample.txt")
