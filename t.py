import asyncio
import aiomysql
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

async def save_data():
    async with aiomysql.connect(user='skf', password='123456') as db:
        async with db.cursor() as cursor:
            name = 11
            introduction = 11
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
                
asyncio.run(save_data())
