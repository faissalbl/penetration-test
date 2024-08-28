#!//usr/bin/python3

import socket

defaultTimeout = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(defaultTimeout)

def portScanner(ip, port):
    if s.connect_ex((ip, port)):
        print("The port is closed")
    else:
        print("The port is open")

def getInput():
    try:
        ip = input("What IP you want to scan? ")
        port = int(input("What port you want to scan? "))
        return ip, port
    except ValueError:
        print("Invalid ip or port entered. Please try again.")
        return getInput()

ip, port = getInput()

print("IP: {}, port: {}".format(ip, port))

portScanner(ip, port)



