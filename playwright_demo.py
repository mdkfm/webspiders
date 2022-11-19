from playwright.sync_api import sync_playwright
import asyncio
from playwright.async_api import async_playwright

'''API
page.click(selector, **kwargs)
page.fill(selector, value, **kwargs)
page.get_attribute(selector, name, **kwargs)
'''

def seletor_test(page):
	#css + text
	page.click("article:has-tetx('Playwright')") #选择包含Playwright字符串的article节点
	page.click("#nav-bar :text('Contact us')") #选择文本为Contact us的nav-bar节点
	
	#css + 节点关系
	page.click(".item-desciption:has(.item-promo-banner)")
	page.click("input:right-of(:text('Username'))")
	
	#xpath
	page.click("xpth=//button") #申明为xpath

def sync_main():
	with sync_playwright() as p:
		browser = p.firefox.launch() #默认启动无头模式
		page = browser.new_page()
		page.goto('https://www.baidu.com')
		page.screenshot(path=f'screenshot.png')
		print(page.title())
		browser.close()

async def async_main():
	async with async_playwright() as p:
		browser = await p.firefox.launch()
		page = await browser.new_page()
		await page.goto('https://www.baidu.com')
		await page.screenshot(path=f'screenshot.png')
		print(await page.title())
		await browser.close()

def devices_test():
	with sync_playwright() as p:
		iphone = p.devices['iPhone 12 Pro Max'] #模拟移动端
		browser = p.webkit.launch(headless=False)
		context = browser.new_context(**iphone, locale='zh-CN') #传入iphone参数
		page = context.new_page()
		page.goto('https://www.whatismybrowser.com/')
		page.wait_for_load_state(state='networkidle')
		page.screenshot(path='browser-iphone.png')
		browser.close()

def on_response(response):
	#事件监听
	if '/api/movie/' in response.url and response.status == 200:
		print(response.json())

def on_test():
	with sync_playwright() as p:
		browser = p.firefox.launch(headless=False)
		page = browser.new_page()
		page.on('response', on_response)
		page.goto('https://spa6.scrape.center/')
		page.wait_for_load_state(state='networkidle')
		browser.close()

def query_test():
	with sync_playwright() as p:
		browser = p.firefox.launch(headless=False)
		page = browser.new_page()
		page.goto('https://spa6.scrape.center/')
		page.wait_for_load_state(state='networkidle')
		elements = page.query_selector_all('a.name') #获取多个节点
		for element in elements:
			print(element.get_attribute('href'))
			print(element.text_content())
		browser.close()
	
