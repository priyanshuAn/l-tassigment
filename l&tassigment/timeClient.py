# import socket
# s = socket.socket()
# host = socket.gethostname()
# port = 12345
 
# s.connect((host, port))
 
   
# print (s.recv(1024).decode())  
# s.close()

import socket

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend   ,serverAddressPort)
# Send to server using created UDP socket
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])

print(msg)