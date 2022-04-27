#!/usr/bin/python3

import sys
import os 

import cgi, cgitb 



print( "Cache-Control: no-cache")
print( "Content-type: text/html\n\n")

# Body - HTML
print("<html>")
print("<head><title>Python Sessions</title></head>\n")
print("<body>")
print("<h1>Python Sessions Page 2</h1>")
print("<table>")


name = None 
if 'HTTP_COOKIE' in os.environ: 
    cookie =  os.environ["HTTP_COOKIE"]
    cookies = cookie.split(";")
    username = cookies[2]
    name = username

    if 'destroyed' in name: 
        name = None 


if name is not None: 
    print("<tr><td>Cookie:</td><td>%s</td></tr>\n"%name )
else: 
    print("<tr><td>Cookie:</td><td>None</td></tr>\n")

    
# Links for other pages
print("<br />")
print("<a href=\"/cgi-bin/py-sessions-1.py\">Session Page 1</a>")
print("<br />")
print("<a href=\"/py-cgiform.html\">py CGI Form</a>")
print("<br /><br />")

# Destroy Cookie button
print("<form action=\"/cgi-bin/py-destroy-session.py\" method=\"get\">")
print("<button type=\"submit\">Destroy Session</button>")
print("</form>")



print( "</body>")
print( "</html>")