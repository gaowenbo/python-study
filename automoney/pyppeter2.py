
import asyncio
from pyppeteer import launch
import sched
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from browsermobproxy import Server
from loguru import logger
import _thread

logger.add("d:\\python\\target\\pypperdebug{time}.log", encoding="utf-8")

async def main():
    args = []
    args.append('--disable-gpu')
    args.append('--user-data-dir={0}'.format("D:\\ssss"))
    args.append('--ignore-certificate-errors')
    browser = await launch(headless=False, args=args)
    page = await browser.newPage()
    await page.goto("https://qq.com")
    await page.screenshot({'path': 'example.png'})
    await page.goto("https://www.baidu.com")
    return page

get_future = asyncio.ensure_future(main())
asyncio.get_event_loop().run_until_complete(get_future)
page = get_future.result()

