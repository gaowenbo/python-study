from selenium import webdriver
from selenium.webdriver.support.select import Select

def toIdc(driver: webdriver.Chrome):
    driver.execute_script("window.open('http://idcenter.box.zonghengke.com/')")
    driver.switch_to.window(driver.window_handles[-1])
    if (len(driver.find_elements_by_id("in_user_Nm")) > 0):
        driver.find_element_by_id("in_user_Nm").send_keys("gaowenbo")
        driver.find_element_by_id("in_password").send_keys("YKUacrVjlfoR")
        driver.find_element_by_id("sign_in").click()

def toIdcL(driver: webdriver.Chrome):
    driver.execute_script("window.open('http://idcenter.yunzong.me/idcenter/')")
    driver.switch_to.window(driver.window_handles[-1])
    if (len(driver.find_elements_by_id("in_user_Nm")) > 0):
        driver.find_element_by_id("in_user_Nm").send_keys("gaowenbo")
        driver.find_element_by_id("in_password").send_keys("YKUacrVjlfoR")
        driver.find_element_by_id("sign_in").click()

def toCe(driver: webdriver.Chrome):
    toIdcL(driver)
    driver.get("http://cloudengine.yunzong.me:10470")

def toService(driver: webdriver.Chrome, serviceName: str):
    toCe(driver)
    driver.get("http://cloudengine.yunzong.me:10470/apply/list#allApplyInfo")
    Select(driver.find_elements_by_id("select2-button-addons-single-input-group-sm")[1]).select_by_visible_text("zys-pay")

