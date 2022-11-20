import asyncio
from playwright.async_api import async_playwright
import aiomysql
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
DETAIL_URL = 'https://spa2.scrape.center{href}'
TIMEOUT = 10
TOTAL_PAGE = 10
# ~ CONCURRENCY = 5
# ~ semaphore = asyncio.Semaphore(CONCURRENCY)

async def on_response(response):
	if '/api/movie/' in response.url and response.status == 200:
		return await response.json()
	
async def scrape_detail(href, browser):
	async with await browser.new_context() as context:
		url = DETAIL_URL.format(href=href)
		page = await context.new_page()
		await page.on('response', on_response)
		await page.goto(url)
		logging.info('scrape detail %s', url)

async def scrape_index(page, browser):
	async with await browser.new_context() as context:
		url =  INDEX_URL.format(page=page)
		page = await context.new_page()
		await page.goto(url)
		await page.wait_for_load_state(state='networkidle')
		elements = page.query_selector_all('a.name')
		logging.info('scrape index %s', url)
		hrefs = []
		for element in elements:
			hrefs.append(element.get_attribute('href'))
		return hrefs

async def main_scrape(page, browser):
	hrefs = await scrape_index(page, browser)
	for href in hrefs:
		detail_data = await scrape_detail(href, browser)
		print(detail_data)

async def main():
	async with async_playwright() as playwright:
		browser = await playwright.firefox.launch()
		tasks = [main_scrape(page, browser) for page in range(1, TOTAL_PAGE + 1)]
		await asyncio.gather(*tasks)

asyncio.run(main())
