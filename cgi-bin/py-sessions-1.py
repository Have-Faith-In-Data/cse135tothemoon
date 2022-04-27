#!/usr/bin/python3

import sys
import os 
import cgi, cgitb 





print( "Cache-Control: no-cache")
print( "Content-type: text/html\n")


username = sys.stdin.readlines() 
if len(username) > 0: 
    print("Set-Cookie: %s\n\n"%username)


# Headers
print( "<html>")
print( "<head>")
print( "<title>Python Sessions</title>")
print( "</head>")
# Body - HTML 
print( "<body>")

print( "<h1>Sessions Page 1</h1>")


print("<table>")
if len(username) > 0 : 
    print("<tr><td>Cookie:</td><td>",username,"</td></tr>\n")
elif "HTTP_COOKIE" in os.environ  and os.environ["HTTP_COOKIE"] == "destroyed":
    print("<tr><td>Cookie:</td><td>",os.environ["HTTP_COOKIE"],"</td></tr>\n")
else: 
    print("<tr><td>Cookie:</td><td>None</td></tr>\n")
print("</table>")

# Links for other pages
print("<br />")
print("<a href=\"/cgi-bin/py-sessions-2.py\">Session Page 2</a>")
print("<br />")
print("<a href=\"/py-cgiform.html\">py CGI Form</a>")
print("<br /><br />")

# Destroy Cookie button
print("<form action=\"/cgi-bin/py-destroy-session.py\" method=\"get\">")
print("<button type=\"submit\">Destroy Session</button>")
print("</form>")



print( "</body>")
print( "</html>")

#  https://www.tutorialspoint.com/How-to-process-a-simple-form-data-using-Python-CGI-script
