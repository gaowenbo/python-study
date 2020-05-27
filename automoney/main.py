import time
import sys
import pyautogui
import random
import _thread

pyautogui.FAILSAFE = False


def upFunction():
    def DoA1():
        try:
            curX, curY = pyautogui.position()
            pyautogui.typewrite("w")
            pic_3 = pyautogui.screenshot("my_screenshot.png", region=(0, 0, 300, 400))
        except KeyboardInterrupt:
            sys.exit(0)

    while True:
        DoA1()
        time.sleep(random.randint(15, 30))


def clickFun():
    def DoA():
        try:
            pyautogui.click(300, 400)
            pic_3 = pyautogui.screenshot("my_screenshot2.png", region=(0, 0, 300, 400))
        except KeyboardInterrupt:
            sys.exit(0)

    while True:
        DoA()
        time.sleep(random.randint(180, 182))


_thread.start_new_thread(upFunction, ())
_thread.start_new_thread(clickFun, ())

while 1:
   pass
