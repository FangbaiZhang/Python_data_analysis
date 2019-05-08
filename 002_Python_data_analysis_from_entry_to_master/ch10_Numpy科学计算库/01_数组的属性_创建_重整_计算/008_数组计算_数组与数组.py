# -*- coding:utf-8 -*-
# 数组计算，数组中每个值都会被计算

import numpy as np

# 生成二个形状一样的二维数组
t1 = np.arange(12).reshape((3, 4))
t2 = np.arange(100, 112).reshape((3, 4))
print(t1)
print()
print(t2)

# 数组一模一样，相同位置的数字进行计算
t3 = t1 + t2
print()
print(t3)

# 生成一个形状不同的数组
t4 = np.arange(0, 3).reshape((3, 1))
print()
print(t4)

# 维度不同的数组计算，只能和一列或者一行进行计算，并且行或列元素相同
# 元素少的每个元素都要被计算
# t1的每一列都要减掉t4中的一列，列中元素都为3个
t5 = t1 - t4
print()
print(t5)

