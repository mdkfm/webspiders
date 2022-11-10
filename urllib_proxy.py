from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

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
