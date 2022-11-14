import asyncio
import aiomysql
import sqlalchemy
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

