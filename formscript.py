import cgi

form = cgi.FieldStorage()
print('Content-type: text/html\n')

if form.has_key('title'):
	title = form['title']
	print title