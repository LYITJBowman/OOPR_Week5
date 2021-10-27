#
# File        : lecturer_Class.py  
# Created     : 26/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

from Question_One.person_Class import Person

class Lecturer(Person):
    def __init__(self, lecturer_name, lecturer_age):
        super(Lecturer, self).__init__(lecturer_name, lecturer_age)


