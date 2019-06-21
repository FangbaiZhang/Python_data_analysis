# -*- coding:utf-8 -*-
# Page194

import numpy as np

# 生成二维数组
a = np.arange(16).reshape(4, 4)
print(a)
print("*" * 50)

# 对a数组进行转置操作，行变成列
# 以对角线为轴，进行了翻转
b = a.T
print(b)
print("*" * 50)

# transpose方法也可以转置,重新排列轴号
c = a.transpose(1, 0)
print(c)
print("*" * 50)

# swapaxes交换轴,0轴和1轴交换，也可以实现转置效果
d = a.swapaxes(1, 0)
print(d)