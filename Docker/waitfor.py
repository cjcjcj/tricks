#!/usr/bin/python

import socket
import time
import os
import sys


addr, port = sys.argv[1], sys.argv[2]
port = int(port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect((addr, port))
        s.close()
        break
    except socket.error as ex:
        time.sleep(.5)
