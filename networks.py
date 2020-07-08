import socket as s
from socket import *

mysocket = s.socket(s.AF_INET,s.SOCK_STREAM)
mysocket.connect(('104.31.80.213', 443))
cmd = 'GET https://www.tempoeficaz.com HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)


while(True):
    data = mysocket.recv(1024)
    if (len(data)  < 1): break
    print(data.decode()) 
mysocket.close()