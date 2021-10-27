#
# File        : abc_cls.py  
# Created     : 26/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
from abc import ABCMeta

class ABS_CLS(metaclass=ABCMeta):
    #Abstract class for all VMs.  Based on Abstract Base Class

    def calc_proc_speed(self):
        pass

    def some_method(self):
        pass