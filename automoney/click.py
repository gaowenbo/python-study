import time
import sys
import pyautogui
import random

pyautogui.FAILSAFE = False


def DoA():
    try:
        pyautogui.click(300, 400)
        pic_3 = pyautogui.screenshot("my_screenshot2.png", region=(0, 0, 300, 400))
    except KeyboardInterrupt:
        sys.exit(0)


while True:
    DoA()
    time.sleep(random.randint(180, 182))
