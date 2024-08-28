#!//usr/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    buffer = 1024
    result = s.recv(buffer).decode()
    s.close()
    return result

def main():
    ip = input("Please enter the ip: ")
    port = int(input("Please enter the port number: "))
    print("grabbing banner for ip: {}, port: {}".format(ip, port))
    print(banner(ip, port))

main()