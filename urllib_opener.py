from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError, HTTPError

username = 'admin'
pswd = 'admin'
url = 'http://ssr3.scrape.center/'

def BasicAuthHandler(url:'str', username:'str', pswd:'str')
	p = HTTPPasswordMgrWithDefaultRealm()
	p.add_password(None, url, username, pswd)
	auth_handler = HTTPBasicAuthHandler(p)
	opener = build_opener(auth_handler)

	try:
		result = opener.open(url, timeout=2)
		html = result.read().decode('utf-8')
		print(html)
	except URLError as e:
		print(e.reason)
		
try:
	result = openner.open(url)
	html = result.read().decode('utf-8')
	print(html)
 except HTTPError as e:
	print(e.reason, e.code, e.headers, sep='\n')
except URLError as e:
	print(e.reason)
	
