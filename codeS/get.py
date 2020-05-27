import json
import pandas as pd


data = pd.read_excel("d:\\python\\source\\fk.xlsx", sheet_name=2)

code1 = []
code2 = []
for line in data.values:
    code1.append("\t\t//{}".format(line[4]))
    l = line[1][0].upper() + line[1][1:]
    code2.append("zysSupplierUserVo.set{}({});".format(str(l), line[1]))
    if line[3] == "string":
        code1.append("String {} = jsonObject.getString(\"{}\");".format(line[1], line[1]))
    elif line[3] == "int":
        code1.append("Integer {} = jsonObject.getInteger(\"{}\");".format(line[1], line[1]))
    elif line[3] == "long":
        code1.append("Long {} = jsonObject.getLong(\"{}\");".format(line[1], line[1]))
print("\n".join(code1))
print("ZysSupplierUserVo zysSupplierUserVo = new ZysSupplierUserVo();")
print("\n".join(code2))