#
# File        : student_Class.py
# Created     : 26/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
from Question_One.person_Class import Person

class Student(Person):

    def __init__(self, studentName, studentAge):
        super(Student, self).__init__(studentName, studentAge)

    def attendCollege(self):
        print("{} attends college.".format(self.person_name))

    def sitExams(self):
        print("{} has yet to sit any exams.".format(self.person_name))