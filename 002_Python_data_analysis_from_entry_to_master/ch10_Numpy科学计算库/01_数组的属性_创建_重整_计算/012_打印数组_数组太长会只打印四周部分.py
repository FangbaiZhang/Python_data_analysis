# -*- coding:utf-8 -*-
# Page183

# 一维数组，以行的形式打印
# 二维数组，以矩阵方式打印
# 三维数组，以嵌套矩阵方式打印

import numpy as np

# 一维数组
t1 = np.arange(10000)
print(t1)
print("*" * 50)


# 二维数组,100行100列
t2 = np.arange(10000).reshape(100, 100)
print(t2)
print("*" * 50)

# 三维数组，5个块，10行20列
t3 = np.arange(10000).reshape(5, 10, 200)
print(t3)