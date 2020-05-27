
from pyppeteer import page
import asyncio

def toIdc(driver: page.Page):
    driver.goto("https://www.baidu.com")

