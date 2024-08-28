#!//usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 3001

print("host: {}, port: {}".format(host, port))

serversocket.bind((host, port))

simultaneousConnections = 3

serversocket.listen(simultaneousConnections)

while True:
    clientSocket, address = serversocket.accept()

    print("received connection from {}".format(address))

    message = "Hello! Thank you for connecting to this server." + "\r\n"
    clientSocket.send(message.encode())

    clientSocket.close();
