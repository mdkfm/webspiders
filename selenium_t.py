from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions

import selenium.common.exceptions as Error

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

import time

browser = webdriver.Firefox()

def find_t():
	browser.get('https://www.taobao.com')
	input1 = browser.find_element(By.ID, 'q')
	input2 = browser.find_element('css selector', '#q')
	input3 = browser.find_element('xpath', '//*[@id="q"]')
	#find_element函数的第一个参数可以为字符串或者By类，用来指定搜寻依据
	print(input1, input2, input3)
	browser.close()
	
def interact_t():
	browser.get('https://www.taobao.com')
	input = browser.find_element(By.ID, 'q')
	input.send_keys('iPhone')
	time.sleep(1)
	input.clear()
	input.send_keys('iPad')
	button = browser.find_element('css selector', '.btn-search')
	button.click()
	browser.close()

def actions_t():
	url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
	browser.get(url)
	browser.switch_to.frame('iframeResult')
	source = browser.find_element('css selector', '#draggable')
	target = browser.find_element('css selector', '#droppable')
	actions = ActionChains(browser)
	actions.drag_and_drop(source, target)
	actions.perform()

def get_attr():
	url = 'https://spa2.scrape.center/'
	browser.get(url)
	logo = browser.find_element('css selector', '.logo-image')
	print(logo)
	print(logo.get_attribute('src'))
	browser.close()

def get_info():
	url = 'https://spa2.scrape.center/'
	browser.get(url)
	input = browser.find_element('css selector', '.logo-title')
	print(input.text)
	print(input.id)
	print(input.location)
	print(input.tag_name)
	print(input.size)
	browser.close()

def switch_frame():
	url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
	browser.get(url)
	browser.switch_to.frame('iframeResult')
	try:
		logo = browser.find_element('css selector', '.logo')
	except NoSuchElementException:
		print('NO LOGO')
	browser.switch_to.parent_frame()
	logo = browser.find_element('css slector', '.logo')
	print(logo)
	print(logo.text)
	browser.close()

def wait():
	browser.get('https://www.taobao.com/')
	wait = WebDriverWait(browser, 10)
	input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
	button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
	print(input, button)
	browser.close()

def forward_and_back():
	browser.get('https://www.baidu.com/')
	browser.get('https://www.taobao.com/')
	browser.get('https://www.github.com/')
	browser.back()
	time.sleep(1)
	browser.forward()
	browser.close()

def get_cookie():
	browser.get('https://www.zhihu.com/explore')
	print(browser.get_cookies())
	browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
	print(browser.get_cookies())
	browser.delete_all_cookies()
	print(browser.get_cookies())
	browser.close()

def window_open():
	browser.get('https://www.baidu.com')
	browser.execute_script('window.open()')
	print(browser.window_handles)
	browser.switch_to.window(browser.window_handles[1])
	browser.get('https://www.taobao.com')
	time.sleep(1)
	browser.switch_to.window(browser.window_handles[0])
	browser.get('https://www.github.com')
	browser.get('https://www.baidu.com')
	browser.close()

def error_show():
	for error in sorted(dir(Error)):
		if error.endswith('Exception'):
			print(error)


def prtsc():
	option = FirefoxOptions()
	option.add_argument('--headless')
	browser = webdriver.Firefox(options=option)
	browser.set_window_size(1366, 768)
	browser.get('https://www.baidu.com')
	browser.get_screenshot_as_file('preview.png')
