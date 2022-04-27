#!/usr/bin/python3

import sys
import os 

print( "Cache-Control: no-cache")
print("Set-Cookie: username = destroyed")
print( "Content-type: text/html\n\n")

#Body - HTML
print("<html>")
print("<head><title>py Session Destroyed</title></head>")
print("<body>")
print("<h1>py Session Destroyed</h1>")

print("<br />")
print("<a href=\"/cgi-bin/py-sessions-1.py\">Session Page 1</a>")
print("<br />")
print("<a href=\"/cgi-bin/py-sessions-2.py\">Session Page 2</a>")
print("<a href=\"/py-cgiform.html\">py CGI Form</a>")

print( "</body>")
print( "</html>")