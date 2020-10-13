from os import path,mkdir,listdir
from shutil import copyfile
from loguru import logger
import re

source = "D:\\python\\source\\31"
target = "D:\\python\\so\\target"
import pandas as pd

data = pd.read_excel("d:\\python\\source\\用户照片路径信息2x.xlsx", dtype=str)

print(data)
import requests

def download(one):
    header = {} # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
    r = requests.get("https://canteen.sany.com.cn" + one[1], headers=header, stream=True)
    print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open('D:\\python\\target\\img\\{}.jpg'.format(one[0]), 'wb').write(r.content) # 将内容写入图片
    print("done")
    del r
    print(one)


for one in data.values:
    download(one)