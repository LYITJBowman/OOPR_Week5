#
# File        : os_module_demo.py  
# Created     : 22/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import os

os.path.abspath('.')
os.getcwd()

dir1=os.path.normpath("C:/Users/james/DevOpsCourse/OOPR/Week5")
dir2=os.path.abspath("C:/Users/james/DevOpsCourse/OOPR/Week5")

print("{0}\n{1}".format(dir1, dir2))

while not (os.path.exists("c:\\please_delete_me")):
    os.mkdir("c:\\please_delete_me")