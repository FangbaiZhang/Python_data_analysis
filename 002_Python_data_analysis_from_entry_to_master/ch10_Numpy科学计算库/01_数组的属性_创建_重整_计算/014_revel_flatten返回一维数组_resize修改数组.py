# -*- coding:utf-8 -*-
# Page195

import numpy as np

# 生成二维数组
a = np.arange(16).reshape(4, 4)
print(a)
print("*" * 50)

# 逐行读取返回一维数组的两种方法
b = a.flatten()
print(b)
c = a.ravel()
print(c)

# resize与reshape一样改变数组的形状，但是resize直接修改了原始数组的值，不需要reshape一样赋值
print(a.resize(2, 8)) # 返回值是None
print(a)