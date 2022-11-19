from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import requests

import re
from pyquery import PyQuery as pq

url = 'https://antispider4.scrape.center/css/app.654ba59e.css'
response = requests.get(url)
pattern = re.compile('.icon-(.*?):before\{content:"(.*?)"\}')
results = re.findall(pattern, response.text)
icon_map = {item[0]: item[1] for item in results}

def parse_score(item):
	elements = item('.icon')
	icon_values = []
	for element in elements:
		class_name = (element.attr('class'))
		icon_key = re.search('icon=(\d+)', class_name).group(1)
		icon_value = icon_map.get(icon_key)
		icon_values.append(icon_value)
	return ''.join(icon_values)

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
browser = webdriver.Firefox(options=options)
WebDriverWait(browser, 20) \
    .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = browser.page_source
doc = pq(html)
items = doc('.item')
for item in items.items():
	name = item('.name').text()
	categories = [category.text() for category in item('.categories button').items()]
	score = parse_score(item)
	print(f'name: {name} categories: {categories} score: {score}')
browser.close()
	
