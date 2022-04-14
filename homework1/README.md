## Names of all members in your team:

Haotian Zhang, Shikan Chen

## The password for user "grader" on our Apache server

grader

GiveMeA

## Link to our site

https://www.ucsdcse135sp22.com/

## Details of Github auto deploy setup

Created a webhook on Github repo storing this site code; whenever there is a push acitivity, the webhook will get triggered and send data to the server's auto deploy script; and the script will execute a series of git commands to update the code from GitHub.

## Username/password info for logging into the site

grader

GiveMeA

## Summary of changes to HTML file in DevTools after compression

No matter what kind of space we have added into the website, after compression, the render will stay the same, but all files are compressed into smaller sizes.

## Summary of removing 'server' header

Used mod_security module package, and then changed the server token in apache2.conf to ServerTokens Full and added SecServerSignature “CSE135 Server”. We can restart the server, and the header has been changed by its configuration.

## Extra credit: Analytics configuration
