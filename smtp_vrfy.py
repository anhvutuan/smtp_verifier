#!/usr/bin/python
import socket
import sys
import time

if len(sys.argv) != 2:
    print "Usage: %s  <username wordlist> " % (sys.argv[0])
    sys.exit(0)

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connect = s.connect(('192.168.1.108',25))

# Receive the banner
banner = s.recv(1024)
print "banner: " + banner

file1 = open(sys.argv[1],'r')

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
