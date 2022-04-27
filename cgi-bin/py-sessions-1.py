#!/usr/bin/python3

import sys
import os 
<<<<<<< HEAD
import cgi, cgitb 

# form = cgi.FieldStorage()
# Get data from fields
# username = form.getvalue('username')
# username = ""
=======
>>>>>>> c9a7054be297814f6e902e537f97a6d3c99648be

print( "Cache-Control: no-cache")
print( "Content-type: text/html\n\n")

<<<<<<< HEAD
# if len(username) > 0: 
#     print("Set-Cookie:",username,"\n\n")
=======

username = sys.stdin.readlines() 



if len(username) > 0: 
    print("Set-Cookie:",username,"\n\n")
>>>>>>> c9a7054be297814f6e902e537f97a6d3c99648be



# Headers
print( "<html>")
print( "<head>")
print( "<title>Python Sessions</title>")
print( "</head>")
# Body - HTML 
print( "<body>")

print( "<h1>Sessions Page 1</h1>")
<<<<<<< HEAD
print("<label>")
print("What's Your name?")
print("<input type='text' name='username' autocomplete='off'>")
print("</label>")
print("<input type='submit' value='Test Sessioning'>")



=======
>>>>>>> c9a7054be297814f6e902e537f97a6d3c99648be
print("<table>")
if len(username) > 0 : 
    print("<tr><td>Cookie:</td><td>",username,"</td></tr>\n")
elif os.environ["HTTP_COOKIE"] != None and os.environ["HTTP_COOKIE"] == "destroyed":
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