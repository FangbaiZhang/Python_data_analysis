# -*- coding:utf-8 -*-
# pandas创建Series创建index索引

import pandas as pd
import string

# 创建一个字典
a = {string.ascii_uppercase[i]:i for i in range(10)}

# 字典转换为一维索引数组
b = pd.Series(a)
print(b)

# 取值有两种方法
# 方法1：通过索引的名称(类似字典的键)取值
print(b['A'])
print(b['B'])

# 方法2: 通过索引的位置取值(一维的，类似列表)
print(b[0])
print(b[1])


