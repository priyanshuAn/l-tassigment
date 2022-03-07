import socket
import sys
import json

jsonResult = {"PSNo": "123456"}
jsonResult = json.dumps(jsonResult).encode('utf-8')
try:
    sock = socket.socket()
except socket.error as err:
    print('Socket error because of %s' % (err))

port = 1500
address = "127.0.0.1"

try:
    sock.connect((address, port))
    sock.send(jsonResult)
except socket.gaierror:
    print('There an error resolving the host')
    sys.exit()    
print(jsonResult, 'was sent!')
sock.close()