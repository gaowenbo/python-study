
from pyppeteer.page import Page
import asyncio

def then(promise):
    get_future = asyncio.ensure_future(promise)
    asyncio.get_event_loop().run_until_complete(get_future)
    return get_future.result()

def toIdc(page: Page):
    then(page.goto("http://idcenter.box.zonghengke.com"))
    if len(then(page.JJ("#in_user_Nm"))) > 0:
        then(page.type("#in_user_Nm", "gaowenbo"))
        then(page.type("#in_password", "YKUacrVjlfoR"))
        then(page.click("#sign_in"))

def toCe(page: Page):
    toIdc(page)
    then(page.goto("http://cloudengine.yunzong.me:10470"))

def toService(page: Page):
    toCe(page)
    then(page.frames[1].click("#pageContent > div > div.row > div:nth-child(2) > a"))
    then(page.waitFor(3000))
    then(page.frames[1].click("#pageContent > div > div.row > div > div > div.tabbable.tabbable-tabdrop > ul > li:nth-child(2) > a"))
    then(page.frames[1].click("#allApplyInfo > div > div:nth-child(1) > label:nth-child(1) > div > span > span.selection > span"))
    then(page.frames[1].type("body > span > span > span.select2-search.select2-search--dropdown > input", "zys-pay"))
    then(page.frames[1].click("#select2-select2-button-addons-single-input-group-sm-results > li:contains('zys-pay')"))



# def toService(driver: webdriver.Chrome, serviceName: str):
#     toCe(driver)
#     driver.get("http://cloudengine.yunzong.me:10470/apply/list#allApplyInfo")
#     Select(driver.find_elements_by_id("select2-button-addons-single-input-group-sm")[1]).select_by_visible_text("zys-pay")
#
