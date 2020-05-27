from selenium import webdriver
from loguru import logger
import importlib

logger.add("d:\\python\\target\\seleniu2mdebug{time}.log", encoding="utf-8")

driver = webdriver.Edge()
# driver.get("https://wx.qq.com/?&lang=zh_CN")

import automoney.autopage4
automoney.autopage4.toCe(driver)
