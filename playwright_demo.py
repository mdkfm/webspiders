from playwright.sync_api import sync_playwright

def sync_main():
	with sync_playwright() as p:
		browser = p.firefox.launch() #默认启动无头模式
		page = browser.new_page()
		page.goto('https://www.baidu.com')
		page.screenshot(path=f'screenshot.png')
		print(page.title())
		browser.close()

import asyncio
from playwright.async_api import async_playwright

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

