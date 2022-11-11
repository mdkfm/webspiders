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
