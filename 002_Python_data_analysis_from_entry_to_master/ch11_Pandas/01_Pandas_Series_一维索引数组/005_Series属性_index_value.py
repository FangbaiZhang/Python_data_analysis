# -*- coding:utf-8 -*-
# pandas创建Series创建index索引

import pandas as pd
import string

# 创建一个字典
a = {string.ascii_uppercase[i]:i for i in range(10)}

# 字典转换为一维索引数组
b = pd.Series(a)
# print(b)

# 获取index(键), 可迭代的，类似于一个列表
print(b.index)
print(type(b.index))
for i in b.index[0:3]:
    print(i)

# 获取values(值)
print(b.values)
print(type(b.values))
for i in b.values[:3]:
    print(i)