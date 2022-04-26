#!/usr/bin/python3

from datetime import datetime
import socket
import os 

print( "Cache-Control: no-cache")
print( "Content-type: text/html\n\n")
print( "<html>")
print( "<head>")
print( "<title>Environment Variables</title>")
print( "</head>")
print( "<body>")

print( "<h1>Environment Variables</h1>")

for i in os.environ.keys(): 
    print(i,":",os.environ[i],"<br />\n" )

print( "</body>")
print( "</html>")