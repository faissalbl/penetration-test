#!//usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '10.0.2.15'
port = 3001

print("connecting to host: {}, port: {}".format(host, port))

clientsocket.connect((host, port))

buffer = 1024

message = clientsocket.recv(buffer)

clientsocket.close()

print(message.decode())