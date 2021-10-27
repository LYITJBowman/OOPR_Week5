#
# File        : zip_demo.py  
# Created     : 22/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import zipfile, os

def zip_file_processing():
    os.chdir(os.path.normpath("C://Temp//ZipDemo"))
    newZip = zipfile.ZipFile('myNew.zip', 'a')
    newZip.write("Blah.txt")

    print("{}".format(newZip.printdir()))

    newZip.write("DeBlah.txt")

    print("\nFiles in the zip are: {}\n".format("c://Temp//ZipDemo//extracthere"))
    newZip.extractall("c://Temp//ZipDemo//extracthere")
    newZip.close()


if __name__ == '__main__':
    zip_file_processing()
