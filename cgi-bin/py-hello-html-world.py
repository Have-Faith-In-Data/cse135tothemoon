#!/usr/bin/python3

from datetime import datetime
import socket

print( "Cache-Control: no-cache")
print( "Content-type: text/html\n\n")
print( "<html>")
print( "<head>")
print( "<title>Hello, Python!</title>")
print( "</head>")
print( "<body>")

print( "<h1>Steve and Jason were here - Hello, Python!</h1>")
print( "<p>This page was generated with the Python programming langauge</p>")

date = datetime.now()  
print( "<p>Current Time: {d}</p>".format(d = date))

# IP Address is an environment variable when using CGI
address = socket.gethostbyname(socket.gethostname())
print( "<p>Your IP Address: {a}</p>".format(a=address))

print( "</body>")
print( "</html>")