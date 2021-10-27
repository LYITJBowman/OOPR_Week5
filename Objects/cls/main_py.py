#
# File        : main_py.py  
# Created     : 25/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

from cls.vm_Class import VM
from cls.win_vm import WINVM
from cls.abc_cls import ABS_CLS

vm1 = VM(1,"Michael")
vm2 = VM(2,"Clodagh")

vm1.print_vm_details()
vm2.print_vm_details()

vm1.print_total_vms()
vm2.print_total_vms()

print("\n")
vm3 = WINVM('QA', 'KB0102321')
vm3.print_dept()
vm3.print_vm_details()
vm3.print_total_vms()

vm3.__str__()

vm3.verify_compliance(10)
vm3.verify_compliance(10, "Security")

ABS_CLS.register(WINVM)

ans=issubclass(WINVM, ABS_CLS)
print("WINVM is now a subclass of ABS_CLS: {}".format(ans))
ans=issubclass(VM,ABS_CLS)
print("VM is now a subclass of ABS_CLS: {}".format(ans))
ans=isinstance(vm3, ABS_CLS)
print("vm3 is an instance of ABS_CLS: {}".format(ans))