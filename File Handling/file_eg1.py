#
# File        : file_eg1.py
# Created     : 21/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def file_processing(file_name):
    """
    Opem a file with a list of students and print their details.

    :param
    file_name: Name of the file with students name, lnumber and course details

    :return:
    Nothing
    """

    lines = open(file_name).readlines()

    for line in lines:
        student, l_num, course = line.split(",")
        print("Student Name:\t{0} \nLNumber:\t\t{1} \nCourse:\t\t\t{2}\n".format(student, l_num, course))

if __name__ == '__main__':
    file_processing("sample.txt")
