from os import path,mkdir,listdir
from shutil import copyfile
from loguru import logger

import base64
print(base64.b64decode("ztLKx9fWt/u0rg=="))

logger.add("info.log", encoding="utf-8")
logger.info("开始...")

source = "source"
target = "target"

if not path.exists(source):
    logger.error("source 目录不存在")

fileList = listdir(source)
new_file = open("wenjian.txt","w",encoding="utf-8")

num = 0
total = 0
name = []
for s in fileList:
    #如果有下划线,则去掉
    targetName = s

    new_file.writelines(targetName + "\n")
    index = s.find("_")
    indexdian = s.find(".")
    if index > 0:
        targetName = s[0:index] + s[indexdian:]

    indexdian = targetName.find(".")
    if indexdian == 4:
        targetName = "0000" + targetName

    indexdian = targetName.find(".")
    if indexdian != 8:
        name.append(targetName)
    total += 1
    logger.info("处理"+ s + "->" + targetName)

new_file.close()

# for s in code:
#     end_pos = s.rfind('.') - 1  # 倒数第一个"/"的位置再左移一位
#     start_pos = s.rfind('.', 0, end_pos)
#     path = s[0:start_pos].replace(".", "\\") + "\\"
#     if (not path.exists(target + path)):
#         makedirs(target + path)
#     if (path.exists(source + path + s[start_pos + 1:])):
#         old_file = open(source + path + s[start_pos + 1:],"r",encoding="utf-8")
#         lines = old_file.readlines()
#         old_file.close()
#         new_file = open(target + path + s[start_pos + 1:],"w",encoding="utf-8")
#         new_file.writelines(lines)
#         new_file.close()
#         print("文件" + source + path + s[start_pos + 1:] + "拷贝成功行数:" + str(len(lines)))
#         num += 1
#         total += len(lines)
#     else:
#         print("文件" + source + path + s[start_pos + 1:] + "不存在")

# print("共" + str(len(code))+ "成功" + str(num) + "总行数" + str(total))


