#
# File        : JSON_Reader.py  
# Created     : 25/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

import json

def parse_student_json(file_name):
    fh = open(file_name)
    for line in fh:
        raw_data = json.loads(line)
        print("{}".format(raw_data['first_name']))

def parse_provisioner_json_data(file_name):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)

    print(type(data))
    print(data)

    provisioner_details = data["resource"]["aws_instance"]["example"]["provisioner"]
    print("Provisioner Details: {}".format((provisioner_details)))
    print("\n\nItems in Provisioner List:")
    for item in provisioner_details:
        print(item, "\n")

if __name__ == '__main__':
    parse_student_json("jsons")
    # parse_provisioner_json_data("provisioner.json")
    new_data = {"student_id": "L000223344", "first_name": "Jo", "last_name": "Michaels"}
    print(new_data)
    with open("jsons", "a") as write_file:
        write_file.write('\n')
        json.dump(new_data, write_file)