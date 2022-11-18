import asyncio
from pyppeteer import launch
from pyquery import PyQuery as py

async def main1():
	browser = await launch()
	page = await browser.newPage()
	await page.goto('https://spa2.scrape.center/')
	await page.waitForSelector('.item .name')
	doc = pq(await page.content())
	names = [item.text() for item in doc('.item .anme').items()]
	print('Name:', names)
	await brower.close()


width, height = 1366, 768


async def main2():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)
    await page.screenshot(path='example.png')
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')
    
    print(dimensions)
    await browser.close()


asyncio.run(main1())
