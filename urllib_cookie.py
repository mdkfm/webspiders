import http.cookiejar, urllib.request

def Mozilla(url, filename, only_read=True):
	cookie = http.cookiejar.MozillaCookieJar(filename)
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	response = opener.open(url)
	
	if not only_read:
		cookie.save(ignore_discard=True, ignore_expires=True)

	for item in cookie:
		print(item.name + '=' + item.value)


def LWP(url, filename):
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
