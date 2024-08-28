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

match resp:
    case '1':   
        print("Nmap version: ", scanner.nmap_version())
        scanner.scan(ipAddr, "1-1024", "-v -sS", True)
        print(scanner.scaninfo())
        print("scanner keys: ", scanner.all_hosts())
        print("scanner[ipAddr] keys: ", scanner[ipAddr].keys())
        print("IP Status: ", scanner[ipAddr].state())
        print(scanner[ipAddr].all_protocols())
        print("Open Ports: ", scanner[ipAddr]['tcp'].keys())

    case '2':   
        print("Nmap version: ", scanner.nmap_version())
        scanner.scan(ipAddr, "1-1024", "-v -sU", True)
        print(scanner.scaninfo())
        print("scanner keys: ", scanner.all_hosts())
        print("scanner[ipAddr] keys: ", scanner[ipAddr].keys())
        print("IP Status: ", scanner[ipAddr].state())
        print(scanner[ipAddr].all_protocols())
        print("Open Ports: ", scanner[ipAddr]['udp'].keys())

    case '3':   
        print("Nmap version: ", scanner.nmap_version())
        scanner.scan(ipAddr, "1-1024", "-v -sS -sV -sC -A -O", True)
        print(scanner.scaninfo())
        print("scanner keys: ", scanner.all_hosts())
        print("scanner[ipAddr] keys: ", scanner[ipAddr].keys())
        print("IP Status: ", scanner[ipAddr].state())
        print(scanner[ipAddr].all_protocols())
        print("Open Ports: ", scanner[ipAddr]['tcp'].keys())

    case _:
        print("Not a valid option.")
        exit()