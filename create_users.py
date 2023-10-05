#!/usr/bin/python
import os
import re
import sys

def main():
    for line in sys.stdin:
        # looks for '#' at the beginning of a line
        # we want to skip this lines (comments)
        match = re.match(r'^#', line)
        
        # strip any whitespace and split into an array
        fields = line.strip().split(':')
        
        # if a match is found in the regex, or the number of fields don't equal 5, then we skip to the next line in input file
        if match or len(fields) != 5: 
            continue # continute the loop to next iteration

        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[3], fields[2])

        groups = fields[4].split(',')  # Split the fifth field into a list of groups

        print "==> Creating account for %s..." % (username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        #print cmd
        os.system(cmd)  # Execute the command to create a user account
        print "==> Setting the password for %s..." % (username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        #print cmd
        os.system(cmd)  # Execute the command to set the password

        for group in groups: # iterating over the groups lists to assign user to groups
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)  # Execute the command to assign the user to a group

if __name__ == '__main__':
    main()
