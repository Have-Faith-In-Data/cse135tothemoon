#!/usr/bin/python3

import cgi 
import sys 
import os 

print( "Cache-Control: no-cache")
print( "Content-type: text/html\n\n")
print( "<html>")
print( "<head>")
print( "<title>General Echo</title>")
print( "</head>")
print( "<body>")

print( "<h1>General Echo</h1>")
protocol =  os.environ["SERVER_PROTOCOL"]
method = os.environ['REQUEST_METHOD']
body = sys.stdin.readlines()

print("<tr><td>Protocol:</td><td>%s</td></tr>\n"%protocol)
print("<tr><td>Method:</td><td>%s</td></tr>\n"%method)
print("<tr><td>Message Body:</td><td> %s</td></tr>\n"%body)

print( "</body>")
print( "</html>")