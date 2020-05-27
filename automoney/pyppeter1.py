
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

logger.add("d:\\python\\target\\seleniumdebug{time}.log", encoding="utf-8")

server = Server("D:\\aa\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()
proxy.new_har("wx", options={ 'captureContent': True})

schedule = sched.scheduler(time.time, time.sleep)

def sendEmail(subject, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['from'] = Header("tfkb@foxmail.com", "utf-8")
    msg['to'] = Header("948053013@qq.com", "utf-8")  #多个收件人的邮箱应该放在字符串中,用字符分隔, 然后用split()分开,不能放在列表中, 因为要使用encode属性
    msg['subject'] = Header(subject, "utf-8")
    smtp = smtplib.SMTP_SSL('smtp.qq.com',465)#需要一个安全的连接，用SSL的方式去登录得用SMTP_SSL，之前用的是SMTP（）.端口号465或587
    smtp.login("tfkb@foxmail.com","qecetbklydlcbdja")#发送方的邮箱，和授权码（不是邮箱登录密码）
    smtp.sendmail("tfkb@foxmail.com", "948053013@qq.com".split(";"), msg.as_string())#注意, 这里的收件方可以是多个邮箱,用";"分开, 也可以用其他符号
    logger.info("发送成功！")
    smtp.quit()

containUrl = "house.qq.com"

def printl():
    if not str(proxy.har).startswith("{'log':"):
        return
    result = proxy.har["log"]["entries"]
    proxy.new_har("wx", options={ 'captureContent': True})
    for entry in result:
        if str(entry["request"]["url"]).startswith("https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsync"):
            logger.info("l")
            if not dict(entry["response"]["content"]).__contains__('text'):
                continue
            jsons = json.loads(str(entry["response"]["content"]['text']).replace("\\n", "\n"))
            # print(jsons)
            for a in jsons["AddMsgList"]:
                contentR = a["Content"]
                if (contentR == "收到红包，请在手机上查看"):
                    sendEmail(str(a["FromUserName"]), str(a["FromUserName"]))
                logger.info(contentR)
        elif str(entry["request"]["url"]).__contains__(containUrl):
            logger.info(entry)

def printthread():
    while True:
        printl()
        time.sleep(5)


_thread.start_new_thread(printthread, ())

browser = ''
page = ''

print(proxy.proxy)

async def main():
    args = []
    args.append('--proxy-server={0}'.format(proxy.proxy))
    args.append('--disable-gpu')
    args.append('--user-data-dir={0}'.format("D:\\ssss"))
    args.append('--ignore-certificate-errors')
    browser = await launch(headless=False, args=args)
    page = await browser.newPage()
    await page.goto("https://house.qq.com")
    await page.screenshot({'path': 'example.png'})
    return browser

get_future = asyncio.ensure_future(main())
asyncio.get_event_loop().run_until_complete(get_future)
br = get_future.result()


