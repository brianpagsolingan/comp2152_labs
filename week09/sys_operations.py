import platform
import socket
import os
import sys
print(f"Machine Type:{platform.machine()}\n ")
print(f"CPU Architechture: {platform.architecture()}\n")

socket.setdefaulttimeout(50)
print(f"Current default timeout: {socket.getdefaulttimeout()}\n")

print(f"OS Type: {os.name}\n")
print(f"OS Name: {platform.system()}\n")

print(f"Current PID: {os.getpid()}")

file_name = "week09/fdpractice.txt"
file_handler = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"[PID: {os.getpid()}] Opened the file_handle : {file_handler}\n")

file_object_textIO = os.fdopen(file_handler, "w+")
file_object_textIO.write("Some string to write to the file.")
file_object_textIO.flush()

print(f"\n\n[PID: {os.getpid()}] Forking now... \n")
pid = 0

if pid == 0:
    print(f"[Child PID: {os.getpid()}]  [Parent PID: {os.getppid()}]\n")
    os.lseek(file_handler, 0, 0)
    print(f"[Child PID: {os.getpid()}]  [File content: {os.read(file_handler, 100).decode()}]\n") # need do decode because its in binary
    os.close(file_handler)
    sys.exit(0)
else:
    print(f"[Parent PID: {os.getpid()}]  [Parent PID: {pid}]\n")
    print("Wait for child process to finish")
    os.wait()
    print("Child finished")
    file_object_textIO.close()

sys.exit(0)

