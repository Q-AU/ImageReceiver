#!/usr/bin/env python3

import socket
import cv2


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    img=cv2.imread('./sample.jpg')
    data=cv2.resize(img,(1920,1080,4))
    data=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
    cv2.imshow('image',img)
    s.sendall(bytes(data))
    data = s.recv(1024)

print('Received', repr(data))