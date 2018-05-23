#!/opt/python-3.4/linux/bin/python3

import sys
import random
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 65113))
host, port = s.getsockname()  
print("connect to host %s" % gethostbyname(gethostname()))
print("connect to port number %s" % port)

while True:


  print("waiting for connection")
  s.listen(10)

  client, addr = s.accept()
  print("Got a connection from %s" % str(addr))
  
  x = "Hello World!"

  print(x)
  
  client.send(x.encode('ascii'))
  
  client.shutdown(1)      
  client.close()
  print("disconnected!")




