#!/bin/python3

import socket

host = '127.0.0.1'
port = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is a port
 
s.connect((host,port)) #argument is tuple

