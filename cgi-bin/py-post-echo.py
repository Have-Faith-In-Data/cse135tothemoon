#!/usr/bin/python3

import cgi 
import sys 

print( "Cache-Control: no-cache")
print( "Content-type: text/html\n\n")
print( "<html>")
print( "<head>")
print( "<title>POST Message Body</title>")
print( "</head>")
print( "<body>")

print( "<h1>POST Message Body</h1>")
body = sys.stdin.readlines()
print("Message Body:",body,"\n<br/>")

print( "</body>")
print( "</html>")