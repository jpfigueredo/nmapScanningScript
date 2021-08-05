#!usr/bin/python3

import nmap

scanner = nmap.PortScanner()

# Simple NMAP automation script

ipAddress = input("Enter IP for scan: ")
print("IP entered: ", ipAddress)
type(ipAddress)

response = input("""\nChoose SCAN type
1. SYN ACK
2. UDP
3. COMPREHENSIVE\n
Enter Number: """)
print("Option selected: ", response)

if(response == '1'):
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ipAddress, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ipAddress].state())
    print(scanner[ipAddress].allprotocols())
    print("Open ports: ", scanner[ipAddress]['tcp'].keys())
elif(response == '2'):
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ipAddress, '1-1024', '-v -su')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ipAddress].state())
    print(scanner[ipAddress].allprotocols())
    print("Open ports: ", scanner[ipAddress]['udp'].keys())
elif(response == '3'):
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ipAddress, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ipAddress].state())
    print(scanner[ipAddress].allprotocols())
    print("Open ports: ", scanner[ipAddress]['tcp'].keys())
else:
    print("Invalid Option.")
