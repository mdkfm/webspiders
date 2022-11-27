import time
import re
import pytesseract
from io import BytesIO
from PIL import Image
from retrying import retry
from playwright.sync_api import sync_playwright
import numpy as np

'''
效果不好
'''

def preprocess(image):
    image = image.convert('L')
    array = np.array(image)
    array = np.where(array > 50, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    return image


@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login():
    page.goto('https://captcha7.scrape.center/')
    page.wait_for_load_state(state='networkidle')
    page.fill('.username input[type="text"]', 'admin')
    page.fill('.password input[type="password"]', 'admin')
    captcha = page.query_selector('#captcha')
    image = Image.open(BytesIO(captcha.screenshot()))
    image = preprocess(image)
    captcha = pytesseract.image_to_string(image)
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)
    page.fill('.captcha input[type="text"]', captcha)
    page.click('.login')
    try:
        page.wait_for_selector('//h2[contains(., "登录成功")]')
        time.sleep(10)
        page.close()
        browser.close()
        return True
    except TimeoutException:
        return False


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        login()
       
