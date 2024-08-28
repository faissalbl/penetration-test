#!//usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome! This is a simple nmap automation tool.")
print("<--------------------------------------------->")

ipAddr = input("Please enter the IP address you want to scan: ")

print("The IP address entered is: ", ipAddr)

resp = input(''' 
Please enter the type of scan you want to run:
             1) SYN ACK Scan
             2) UDP Scan
             3) Comprehensive Scan
''')

print("You have selected option: ", resp)

timeout = 30

try:
    match resp:
        case '1':   
            scanner.scan(ipAddr, "1-1024", "-v -sS", True, timeout)

        case '2':   
            scanner.scan(ipAddr, "1-1024", "-v -sU", True, timeout)

        case '3':   
            scanner.scan(ipAddr, "1-1024", "-v -sS -sV -sC -A -O", True, timeout)      

        case _:
            print("Not a valid option.")
            exit(1)
except nmap.nmap.PortScannerTimeout:
    print("Scan timed out after ", timeout, " seconds")
    exit(1)

# if the user entered a hostname, get the resulting IP Address
allHosts = scanner.all_hosts()
ipAddr = allHosts[0] if len(allHosts) > 0 else None

if not ipAddr:
    print("The host name is not reachable")
    exit(1)

print("Nmap version: ", scanner.nmap_version())
print(scanner.scaninfo())
print("scanner keys: ", allHosts)
print("scanner[ipAddr] keys: ", scanner[ipAddr].keys())
print("IP Status: ", scanner[ipAddr].state())
protocols = scanner[ipAddr].all_protocols()
print("Protocols: ", protocols)

if 'tcp' in protocols:
    print("Open TCP Ports: ", scanner[ipAddr]['tcp'].keys())

if 'udp' in protocols:
    print("Open UDP Ports: ", scanner[ipAddr]['udp'].keys())
