#!/usr/bin/python3

from datetime import datetime
import socket
import json 


date = datetime.now()  
address = socket.gethostbyname(socket.gethostname())


output = dict() 
output['time'] = date 
output['IP'] = address 
output['heading']= "Hello, Python"
output['title'] = "Hello, Python!"
output['message'] = "This page was generated with the Python programming Lanuage"

optJson = json.dumps(output)
print(optJson)



