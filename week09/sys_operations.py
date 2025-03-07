import platform
import socket
import os
print(f"Machine Type:{platform.machine()}\n ")
print(f"CPU Architechture: {platform.architecture()}\n")

socket.setdefaulttimeout(50)
print(f"Current default timeout: {socket.getdefaulttimeout()}\n")

print(f"OS Type: {os.name}\n")
print(f"OS Name: {platform.system()}\n")

print(f"Current PID: {os.getpid()}")