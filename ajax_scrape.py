import requests
import pymysql
import logging
import json
from os import makedirs
from os.path import exists
import multiprocessing

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
LIMIT = 10
TOTAL_PAGE = 10
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

def create_table():
	db = pymysql.connect(host='localhost', user='skf', password='123456')
	cursor = db.cursor()
	sql = 'CREATE TABLE IF NOT EXISTS spiders.spa1 (name VARCHAR(100) PRIMARY KEY, drama TEXT)'
	try :
		if cursor.execute(sql):
			logging.info('Create table successfuly')
			db.commit()
	except:
		db.rollback()
	db.close()

def save_data(data):
	db = pymysql.connect(host='localhost', user='skf', password='123456')
	cursor = db.cursor()
	name = data.get('name')
	drama = data.get('drama')
	logging.info('detail data %s: %s', name, drama)
	sql = f'INSERT INTO spiders.spa1 VALUES (\'{name}\', \'{drama}\') \
		ON DUPLICATE KEY UPDATE name=\'{name}\', drama=\'{drama}\''
	try:
		if cursor.execute(sql):
			db.commit()
			logging.info('data saved successfully')
	except:
		db.rollback()
		logging.info('save failed')
	db.close()

def main_scrape(page):
	index_data = scrape_index(page)
	for item in index_data.get('results'):
		id = item.get('id')
		detail_data = scrape_detail(id)
		save_data(detail_data)
		
def main():
	create_table()
	pool = multiprocessing.Pool()
	pages = range(1, TOTAL_PAGE + 1)
	pool.map(main_scrape, pages)
	pool.close()

if __name__ == '__main__':
	main()
