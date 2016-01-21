# pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/ 01-20-2016
# copyright Nick Zarczynski

import BaseHTTPServer
import CGIHTTPServer
#import cgitb; cgitb.enable()  ## This line enables CGI error reporting

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8080)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()