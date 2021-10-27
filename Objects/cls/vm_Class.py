#
# File        : vm_Class.py  
# Created     : 25/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

class VM:
    vm_num = 0

    def __init__(self, vm_id, vm_owner):
        self.vm_id = vm_id
        self.vm_owner = vm_owner
        VM.vm_num += 1

    def print_total_vms(self):
        print("There are {} vms in use".format(VM.vm_num))

    def print_vm_details(self):
        print("VM ID: {0}, Owner: {1}".format(self.vm_id, self.vm_owner))