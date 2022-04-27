#!/usr/bin/python3

import cgi 

print( "Cache-Control: no-cache")
print( "Content-type: text/html\n\n")
print( "<html>")
print( "<head>")
print( "<title>get-echo</title>")
print( "</head>")
print( "<body>")

print( "<h1>get-echo</h1>")
arguments = cgi.FieldStorage()

for i in arguments.keys():
    print(arguments[i].value,"<br />\n")
print( "</body>")
print( "</html>")