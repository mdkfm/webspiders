import asyncio
from playwright.async_api import async_playwright
import aiomysql
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
DETAIL_URL = 'https://spa2.scrape.center{href}'
TOTAL_PAGE = 10
CONCURRENCY = 5
semaphore = asyncio.Semaphore(CONCURRENCY)

async def save_data(data):
    async with aiomysql.connect(user='skf0', password='123456') as db:
        async with db.cursor() as cursor:
            name = data.get('name')
            drama = data.get('drama')
            values = (name, drama)
            logging.info('detail data %s: %s', name, drama)
            sql = "INSERT INTO webspiders.spa2 \
                VALUES (%s, %s) \
             ON DUPLICATE KEY UPDATE name=%s, drama=%s"
            try:   
                if await cursor.execute(sql, values*2):
                    await db.commit()
                logging.info('data saved successfully')
            except:
                logging.info('save failed')

async def on_response(response):
    if '/api/movie' in response.url and response.status == 200:
        data = await response.json()
        await save_data(data)
    
async def scrape_detail(href):
    global browser
    url = DETAIL_URL.format(href=href)
    logging.info('scrape detail %s', url)
    page = await browser.new_page()
    page.on('response', on_response)
    await page.goto(url)
    await page.wait_for_load_state(state='networkidle')
    await page.close()
    
async def scrape_index(page):
    global browser
    url =  INDEX_URL.format(page=page)
    logging.info('scrape index %s', url)
    page = await browser.new_page()
    await page.goto(url)
    await page.wait_for_load_state(state='networkidle')
    elements = await page.query_selector_all('a.name')
    hrefs = []
    for element in elements:
        hrefs.append(await element.get_attribute('href'))
    await page.close()
    return hrefs

async def main_scrape(page):
    async with semaphore:
        hrefs = await scrape_index(page)
        for href in hrefs:
            await scrape_detail(href)

async def main():
    async with async_playwright() as playwright:
        global browser
        browser = await playwright.firefox.launch()
        tasks = [main_scrape(page) for page in range(1, TOTAL_PAGE + 1)]
        await asyncio.gather(*tasks)

asyncio.run(main())
