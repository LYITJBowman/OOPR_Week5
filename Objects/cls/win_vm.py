#
# File        : win_vm.py  
# Created     : 25/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
from cls.vm_Class import VM

class WINVM(VM):
    def __init__(self, vm_dept, patch):
        super(WINVM, self).__init__(3, "Ciaran")
        self.vm_dept = vm_dept
        self.patch = patch

    def print_dept(self):
        print("Dept: {0}, Patch: {1}".format(self.vm_dept, self.patch))

    def __str__(self):
        '''Overriding the str method'''
        print("\n__str__ method called")
        print("VM ID: {0}, Owner: {1}".format(self.vm_id, self.vm_owner))
        print("Dept: {0}, Patch: {1}".format(self.vm_dept, self.patch))

    def verify_compliance(self, level, dept="QA"):
        '''Overloading using optional input named dept with default value of QA'''
        print("Verify level {0} by dept {1}".format(level, dept))
