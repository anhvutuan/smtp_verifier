#!/usr/bin/python
#
# This is a simple script that tests if a user exists in a smtp server.
#
import socket
import sys
import time

if len(sys.argv) != 3:
    print "Usage: %s <ip> <username wordlist> " % (sys.argv[0])
    print "Example: %s 192.168.1.108 usernames.txt" % (sys.argv[0])
    sys.exit(0)

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connect = s.connect((sys.argv[1],25))

# Receive the banner
banner = s.recv(1024)
print "banner: " + banner

file1 = open(sys.argv[2],'r')

print "Found users: "

for user in file1:
    # VRFY a user
    s.send('VRFY ' + user )
    result=s.recv(1024)
    #print result
    if "exists" in result:
        print user
    #time.sleep(1)

# Close the Socket
s.close()

print "Search finshed!!\r\n"
