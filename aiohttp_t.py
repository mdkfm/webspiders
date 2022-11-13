import asyncio
import aiohttp
import time

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def post(url, data:'dict'):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            print(await response.text())

async def post_1(url, data:'dict'):
    '''
    convert automatically data into json, and post
    '''
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            print(await response.text())

async def request():
    url = 'https://baidu.com'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response')

async def main():
	start = time.time()
	tasks = [request() for _ in range(10)]
	await asyncio.gather(*tasks)
	end = time.time()
	print('Cost time:', end - start)

if __name__ == '__main__':
	asyncio.run(main())
