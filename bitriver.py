
#define UDP_MESSAGE_PORT 1300
#define MAX_READ_LENGTH  1024

import socket
import sys


def vRunApp():

    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.bind(('',UDP_MESSAGE_PORT))

    print "Listening..."

    while 1:

        data, addr = sock.recvfrom(MAX_READ_LENGTH);

        if len(data) == 0: continue

        print "Message Received From: ", str(addr)

        for i in range(len(data)):
            sys.stdout.write(" ");
            sys.stdout.write(str(hex(ord(data[i]))));

        print

        for i in range(len(data)):
            sys.stdout.write(" ");
            sys.stdout.write(data[i]);

        print

if __name__ == '__main__':
    vRunApp()
