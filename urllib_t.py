import http.cookiejar, urllib.request

def Mozilla_cookie(url, filename, only_read=True):
	cookie = http.cookiejar.MozillaCookieJar(filename)
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	response = opener.open(url)
	
	if not only_read:
		cookie.save(ignore_discard=True, ignore_expires=True)

	for item in cookie:
		print(item.name + '=' + item.value)


def LWP_cookie(url, filename):
	#获取cookie并保存为filename，格式为LWP
	cookie = http.cookiejar.LWPCookieJar(filename)
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	response = opener.open(url)
	
	cookie.save(ignore_discard=True, ignore_expires=True)


def LWP_read(url, filename):
	#从filename中读取cookie
	cookie = http.cookiejar.LWPCookieJar()
	cookie.load(filename, ignore_discard=True, ignore_expires=True)
	
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	response = opener.open(url)
	
	html = response.read().decode('utf-8')
	print(html)

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError, HTTPError

def BasicAuthHandler(url:'str', username:'str', pswd:'str')
	p = HTTPPasswordMgrWithDefaultRealm()
	p.add_password(None, url, username, pswd)
	auth_handler = HTTPBasicAuthHandler(p)
	opener = build_opener(auth_handler)

	try:
		result = opener.open(url, timeout=2)
		html = result.read().decode('utf-8')
		print(html)
	 except HTTPError as e:
	print(e.reason, e.code, e.headers, sep='\n')
	except URLError as e:
		print(e.reason)

from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

def rp_set_url(robots_url, spiders):
	rp = RobotFileParser()
	rp.set_url(robots_url)
	rp.read()
	
	for spider, url in spiders.items():
		print(rp.can_fetch(spiders, url))

def rp_parse(robots_url, spiders):
	rp = RobotFileParser()
	rp.parse(urlopen(robots_url).read().decode('utf-8').split('\n'))
	rp.read()
	
	for spider, url in spiders.items():
		print(rp.can_fetch(spiders, url))

from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

def proxy_test():
	url = 'https://www.baidu.com'
	proxy_hadler = ProxyHandler({
		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	})
	opener = build_opener(proxy_hadler)

	try:
		result = opener.open(url)
		html = result.read().decode('utf-8')
		print(html)
	except URLError as e:
		print(e.reason)
