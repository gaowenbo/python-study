from os import path,mkdir,listdir
from shutil import copyfile
from loguru import logger
import re

source = "D:\\python\\so\\source"
target = "D:\\python\\so\\target"

source = "source"
target = "target"
logger.add("info.log", encoding="utf-8")
logger.info("开始...")
if not path.exists(source):
    logger.error("source 目录不存在")

if not path.exists(target):
    mkdir(target)
fileList = listdir(source)

num = 0
total = 0
name = []
for s in fileList:
    #如果有下划线,则去掉
    targetName = s
    logger.info("处理"+ targetName)
    index = s.find("_")
    indexdian = s.find(".")
    if index > 0:
        targetName = s[0:index] + s[indexdian:]

    indexdian = targetName.find(".")
    re8 = re.compile("^\d{8}$")
    res = re.search(re8, targetName[0:indexdian])
    total += 1
    if res:
        # indexdian = targetName.find(".")
        # if indexdian == 4:
        #     targetName = "0000" + targetName
        #
        # indexdian = targetName.find(".")
        # if indexdian != 8:
        #     name.append(targetName)

        if not path.exists(target + "\\" + targetName):
            copyfile(source + "\\" + s, target + "\\" + targetName)
            num += 1

logger.info("总计:" + str(total) + ",处理后:" + str(num))

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


