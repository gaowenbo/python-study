import re
import os
import os.path
import pandas as pd

data = pd.read_excel("d:\\python\\source\\sa.xlsx")
d = (dict(map(lambda x: ("\"" + x[3] + "\"", (x[1], (x[2]))), data.values)))
print(d)

def changefile(filepath):
    file = open("d:\\python\\source\\service\\" + filepath, "r", encoding="utf-8")
    filew = open("d:\\python\\target\\service\\" + filepath, "w", encoding="utf-8")

    p = re.compile(r"(?<=@HandlerMethodType\().+?(?=\))")
    for f in file.readlines():
        k = p.findall(f)
        if len(k) > 0:
            replace = "value = " + k[0] + ", description = \"" + str(d[k[0]][0]) + "\", apiId = " + str(d[k[0]][1])
            newKey = re.sub(p, replace, f)
            filew.writelines(newKey)
        else:
            filew.writelines(f)


rootdir = "d:\\python\\source\\service\\"
list = os.listdir(rootdir)
for i in range(len(list)):
    changefile(list[i])
