from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

actions_t()

