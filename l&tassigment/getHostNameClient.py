import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))
print(s.recv(1024))
s.close()
import socket
s = socket.socket()
s.connect(("localhost", 9999))
name = input("inter your name")
s.send(bytes(name,'utf-8'))
print(s.recv(1024).decode())