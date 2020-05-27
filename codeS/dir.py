import os


code = ["aa.bb.cc.1.java",
         "aa.bb.cc.2.java",
         ]
source = "d:\\python\\source\\"
target = "d:\\python\\target\\"

num = 0
total = 0
for s in code:
    end_pos = s.rfind('.') - 1  # 倒数第一个"/"的位置再左移一位
    start_pos = s.rfind('.', 0, end_pos)
    path = s[0:start_pos].replace(".", "\\") + "\\"
    if (not os.path.exists(target + path)):
        os.makedirs(target + path)
    if (os.path.exists(source + path + s[start_pos + 1:])):
        old_file = open(source + path + s[start_pos + 1:],"r",encoding="utf-8")
        lines = old_file.readlines()
        old_file.close()
        new_file = open(target + path + s[start_pos + 1:],"w",encoding="utf-8")
        new_file.writelines(lines)
        new_file.close()
        print("文件" + source + path + s[start_pos + 1:] + "拷贝成功行数:" + str(len(lines)))
        num += 1
        total += len(lines)
    else:
        print("文件" + source + path + s[start_pos + 1:] + "不存在")

print("共" + str(len(code))+ "成功" + str(num) + "总行数" + str(total))


