#!/usr/bin/env python
from __future__ import print_function
import os, json, cgi, sys

print('Content-type: text/html\r\n\r\n', end='')

enviroStr = json.dumps(dict(os.environ), indent=4)

form = cgi.FieldStorage()

print(
"""
<html><body>
<h1>Some heading</h1>
<form method='get'><input name='x'></form>
<br>
x was: {0}
<br><br>
{1}
</body></html>
""".format(cgi.escape(str(form.getvalue('x'))), enviroStr)
)