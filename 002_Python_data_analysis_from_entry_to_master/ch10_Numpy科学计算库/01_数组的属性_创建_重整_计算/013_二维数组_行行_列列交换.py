# -*- coding:utf-8 -*-

import numpy as np

# 生成二维数组
a = np.arange(16).reshape(4, 4)
print(a)
print("*" * 50)

# 行行交换，单个中括号取的元素，加一个中括号取的才是行列
a[[1, 2], :] = a[[2, 1], :]
print(a)
print("*" * 50)

# 列列交换
a[:, [0, 2]] = a[:,[2, 0]]
print(a)