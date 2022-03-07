import socket
sock = socket.socket()
print("Socket created...")

port = 1500
address = '127.0.0.1'
sock.bind((address, port))
sock.listen(5)

print('socket is listening')

while True:
   c, addr = sock.accept()
   print('got connection from', addr)
   jsonReceived = c.recv(1024)
   print('json received -->', jsonReceived)
   c.close()