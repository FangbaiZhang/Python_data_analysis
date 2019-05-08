# -*- coding:utf-8 -*-

import numpy as np
# 用于线性代数的模块
import numpy.linalg as LA

a = np.arange(1, 10).reshape(3, 3)
print(a)
print("*" * 50)

# 求矩阵的逆矩阵，注意，原矩阵行列相同
# 设A是数域上的一个n阶矩阵，若在相同数域上存在另一个n阶矩阵B，
# 使得： AB=BA=E ，则我们称B是A的逆矩阵，而A则被称为可逆矩阵
b = LA.inv(a)
print(b)

