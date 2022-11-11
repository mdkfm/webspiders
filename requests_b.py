import requests
from request import Request, Session

def get_bfile(url, filename):
	r = requests.get(url)
	with open(filename, 'wb') as f:
		f.write(r.content)

def post_bfile(url, filename):
	files = {'file': open(filename, 'rb')}
	r =requests.post(url, files=files)
	print(r.text)

def BasicAuth(url, username, password):
	r = requests.get(url, auth=(username, password))
	print(r.status_code)

def set_proxies(url, proxies:'dict'):
	#设置代理
	r = requests.get(url, proxies=proxies)
	print(r.status_code)

def get_session(url, data:'dict'):
	s = requests.Session()
	s.post(url, data=data)
	r = s.get(url)
	print(r.text)

def verify_set(url):
	#关闭ssl证书验证
	response = requests.get(url, verify=False)
	print(response.status_code)

def creative_Request(url, access, data:'dict', headers:'dict'):
	s = Session()
	req = Request(access, url, data=data, headers=headers)
	prepped = s.prepare_request(req)
	r = s.send(prepped)
	print(r.text)
