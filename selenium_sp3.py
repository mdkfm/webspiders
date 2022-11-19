from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pyquery import PyQuery as pq

import re

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
browser = webdriver.Firefox(options=options)

def parse_name(name_html):
	chars = name_html('.char')
	items = []
	for char in chars.items():
		items.append({
			'text': char.text().strip(),
			'left': int(re.search('(\d+)px', char.attr('styles')).group(1))
			})
		items = sotred(items, key=lambda x: x['left'], reverse=False)
		return ''.join([item.get('text') for item in items])

browser.get('https://antispider3.scrape.center/')
WebDriverWait(browser, 10) \
    .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = browser.page_source
doc = pq(html)
names = doc('.item .name')
for name_html in names.items():
	name = parse_name(name_html)
	print(name)
browser.close()
