# -*- coding:utf-8 -*-
# pandas创建Series创建index索引

import pandas as pd
import string

# 创建一个字典
a = {string.ascii_uppercase[i]:i for i in range(10)}

# 字典转换为一维索引数组
b = pd.Series(a)
print(b)

# 取前三行
print(b[0:3])

# 取多行，特定步长
print(b[0:8:2])

# 取多行，指定行数，用两个中括号
print(b[[0, 3, 6]])
print(b[['A', 'B', 'C']])

# 指定条件，只取后面几行，不推荐，推荐使用列表切片
print(b[b>5])

