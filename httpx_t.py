import httpx
import asyncio

def http2(url):
	with httpx.Client(http2=True) as client:
		response = client.get(url)
		print(response.text)

async def fetch(url):
	async with httpx.AsyncClient(http2=True) as client:
		response = await client.get(url)
		print(response.text)

def main(url):
	asyncio.get_event_loop().run_until_complete(fetch(url))
