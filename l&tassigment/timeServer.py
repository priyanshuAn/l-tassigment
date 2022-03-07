# import socket    
# import datetime

# s = socket.socket()    
# host = socket.gethostname() 
# port = 12345
 

# s.bind((host, port))  
 
# s.listen(5) 
        
# while True:
#    c, addr = s.accept()       
#    print ('got connection from addr', addr)
#    date = datetime.datetime.now() 
#    d = str(date)
 
   
#    c.send(d.encode())     
#    c.close()


import socket
import datetime
 

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams

while(True):

    # Sending a reply to client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    date = datetime.datetime.now() 
    d = str(date)

    UDPServerSocket.sendto(d.encode(), address)