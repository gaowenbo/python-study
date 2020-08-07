
import asyncio
from pyppeteer import launch
import importlib
import automoney.autopyppeteer as to
import sched
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from browsermobproxy import Server
from loguru import logger
import tkinter
tk = tkinter.Tk()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
tk.quit()

logger.add("d:\\python\\target\\pypperdebug{time}.log", encoding="utf-8")

def then(promise):
    get_future = asyncio.ensure_future(promise)
    asyncio.get_event_loop().run_until_complete(get_future)
    return get_future.result()

args = []
args.append('--disable-gpu')
args.append('--user-data-dir={0}'.format("D:\\ssss"))
args.append('--ignore-certificate-errors')
browser = then(launch(headless=False, args=args))
page = then(browser.newPage())
then(page.setViewport(viewport={'width': width, 'height': height}))
then(page.screenshot({'path': 'example.png'}))
then(page.goto("https://www.baidu.com"))

