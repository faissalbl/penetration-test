#!//usr/bin/python3

import socket

defaultTimeout = 10

def banner(ip, port):
    result = ''
    try:
        s = socket.socket()
        s.settimeout(defaultTimeout)
        s.connect((ip, port))
        buffer = 1024
        result = s.recv(buffer).decode()
        s.close()
    except TimeoutError:
        result = "Connection timed out. The default timeout is {} seconds".format(defaultTimeout)
    return result

def main():
    try:
        ip = input("Please enter the ip: ")
        port = int(input("Please enter the port number: "))
        print("grabbing banner for ip: {}, port: {}".format(ip, port))
        print(banner(ip, port))
    except ValueError:
        print("Invalid input. Please enter a valid ip and port")

main()