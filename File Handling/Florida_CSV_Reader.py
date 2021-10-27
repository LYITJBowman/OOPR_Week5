#
# File        : Florida_CSV_Reader.py  
# Created     : 25/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#
import csv


def parse_csv_file(file_name):
    fh = open(file_name)
    fr = csv.reader(fh)

    marion = 0
    pinellas = 0

    for row in fr:
        if fr.line_num == 1:
            continue
        if row[2] == 'MARION COUNTY':
            marion += 1
        if row[2] == 'PINELLAS COUNTY':
            pinellas += 1

    print("Marion has {0} and Pinellas has {1} insurance policies.".format(marion, pinellas))


if __name__ == '__main__':
    parse_csv_file('FL_insurance_sample.csv')
