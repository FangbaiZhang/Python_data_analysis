# -*- coding:utf-8 -*-
# Page177

# array方法用于生成数组，传入参数:列表，元组，有序数据结构
# 生成一维数组可以直接使用arange
# dtype用于查看数组内部元素的类型，不指定默认的是电脑系统的位数

import numpy as np

# 生成一维数组，一个方向(一个轴),可以指定数据类型
t1 = np.arange(12, dtype='int64')
print(t1)
print(t1.dtype)

# 生成二维数组，两个方向(两个轴)
# 列表中只有两组数据
t2 = np.array([[1.1, 2.2, 3], [4, 5, 6]])
print(t2)
print(t2.dtype)

# 生成三维数组，三个方向(三个轴)
# 列表中有两个块，每个块里面又有两组数据
t3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t3)
print(t3.dtype)

# 传入range参数
t4 = np.array(range(6))
print(t4)

# 指定参数为python兼容的bool类型
t5 = np.array([1, 0, 1, 0, 2, 2], dtype=bool)
print(t5)
print(t5.dtype)