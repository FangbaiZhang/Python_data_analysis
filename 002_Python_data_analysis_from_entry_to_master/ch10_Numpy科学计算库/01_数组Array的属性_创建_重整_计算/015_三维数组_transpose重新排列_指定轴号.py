# -*- coding:utf-8 -*-
# Page194

import numpy as np

a = np.arange(24).reshape(2, 4, 3)
print(a)
print("*" * 50)

# 使用transpose重新排列轴号
# 列变为0轴，新的0轴有3个块
# 行还是1轴，4行
# 块变为2轴，2列
# 相当于reshape(2, 4, 3)中的，第一个参数和第三个参数交换
# reshape(3, 4, 2),重新排列轴号和重整形状本质一样

b = a.transpose(2, 1, 0)
print(b)