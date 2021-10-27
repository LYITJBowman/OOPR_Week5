#
# File        : main_py.py  
# Created     : 26/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
from Question_One.person_Class import Person
from Question_One.student_Class import Student
from Question_One.lecturer_Class import Lecturer

student1 = Student("James Bowman", 42)
student2 = Student("Nathan Bowman", 7)
lecturer1 = Lecturer("Maria Hill", 34)

student1.markCA()
student2.attendCollege()
lecturer1.lecture()