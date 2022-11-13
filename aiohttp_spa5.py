import asyncio
import aiohttp
import pymysql
import aiomysql
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

CONCURRENCY = 8
semaphore = asyncio.Semaphore(CONCURRENCY)

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
LIMIT = 18
TOTAL_PAGE = 1

async def scrape_api(url):
    logging.info('scraping %s...', url)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                logging.error('get invalid status code %s while scraping %s',
                              response.status, url)
        except:
            logging.error('error occurred while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return await scrape_api(url)

async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return await scrape_api(url)

async def save_data(data):
    async with aiomysql.connect(user='skf', password='123456') as db:
        async with db.cursor() as cursor:
            name = data.get('name')
            introduction = data.get('introduction')
            logging.info('detail data %s: %s', name, introduction)
            sql = f'INSERT INTO spiders.spa5 \
                VALUES (\'{name}\', \'{introduction}\') \
                ON DUPLICATE KEY UPDATE name=\'{name}\', drama=\'{introduction}\''
            try:
                if await cursor.execute(sql):
                    await db.commit()
                    logging.info('data saved successfully')
            except:
                await db.rollback()
                logging.info('save failed')

async def main_scrape(page):
    async with semaphore:
        index_data = await scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = await scrape_detail(id)
            await save_data(detail_data)

async def main():
    tasks = [main_scrape(page) for page in range(1, TOTAL_PAGE + 1)]
    await asyncio.gather(*tasks)
        
if __name__ == '__main__':
    asyncio.run(main())
