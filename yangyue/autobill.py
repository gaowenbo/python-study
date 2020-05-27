from selenium import webdriver

import json

from browsermobproxy import Server

profile=webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)

driver.get("https://c.dgzq.com.cn:8888")



