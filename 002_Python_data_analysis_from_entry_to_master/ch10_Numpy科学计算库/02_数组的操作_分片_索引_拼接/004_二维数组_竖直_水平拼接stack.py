# -*- coding:utf-8 -*-

import numpy as np

# 生成两个形状一样的二维数组
a = np.arange(16).reshape(2, 8)
print(a)
print("*" * 50)

b = np.arange(16).reshape(2, 8)
print(b)
print("*" * 50)

# 竖直拼接，只能传入一个参数，传入参数是一个元组，
c = np.vstack((a, b))
print(c)
print("*" * 50)

# 水平拼接
d = np.hstack((a, b))
print(d)