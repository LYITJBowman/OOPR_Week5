#
# File        : log_parser.py  
# Created     : 25/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

def parse_log_file(file_name):

    lines = open(file_name).readlines()

    failed_count = 0
    illegal_user_count = 0
    error = 0
    count = 0

    for line in lines:
        #print(line)
        comments = line[35:]

        if comments[0] == 'F':
            failed_count += 1
        elif comments[0] == 'I':
            illegal_user_count += 1
        else:
            error += 1
        count += 1

    return failed_count, illegal_user_count, error, count

if __name__ == '__main__':
    failed, illegal, error, count = parse_log_file("sshd_logon_attempt.txt")
    print("Out of a total of {} lines there was {} failed logins, {} illegal logins and {} errors.".format(count, failed, illegal, error))
