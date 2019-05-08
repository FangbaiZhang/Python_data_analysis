# -*- coding:utf-8 -*-

import numpy as np
# 用于线性代数的模块
import numpy.linalg as LA

# 求解以下线性方程的解
# x1 + 2x2 = 2
# 2x1 - x2 = 4

# 先以x前面的参数生成一个二维数组
A = np.array([[1, 2], [2, -1]])
print(A)
print(A.shape)
print("*" * 50)

# 再将方程右边数字生成一个一维数组
B = np.array([2, 4])

# 求解线性方程，数组里面的值即解
C = LA.solve(A, B)
print(C)
