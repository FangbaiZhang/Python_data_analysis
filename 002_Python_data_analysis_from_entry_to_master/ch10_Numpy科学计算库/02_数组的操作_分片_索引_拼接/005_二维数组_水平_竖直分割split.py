# -*- coding:utf-8 -*-

import numpy as np

# 生成两个形状一样的二维数组
a = np.arange(16).reshape(4, 4)
print(a)
print("*" * 50)

# 水平竖直分割是拼接的反操作
# 竖直分割: 以行分割
# 水平分割: 以列分割

# 竖直分割，指定被分割为几个数组，数要被整除
b = np.vsplit(a, 2)
print(b)
print("*" * 50)

# 水平分割
c = np.hsplit(a, 2)
print(c)
print("*" * 50)

# 也可以直接使用split函数，指定轴号0，作用于列，以行分割，竖直分割列
e = np.split(a, 2, axis=0)
print(e)