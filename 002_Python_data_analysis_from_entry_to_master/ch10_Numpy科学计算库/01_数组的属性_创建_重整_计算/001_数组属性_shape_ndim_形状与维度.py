# -*- coding:utf-8 -*-
# Page175

import numpy as np

# np中的arange返回的是一个ndarray类
# 有三个参数，依次为start，end(不包含)，step。
# 在不指明start或者step的情况下，默认起始点为0，步长为1。
# shape方法查看数组的维度

# 一维数组，一个方向(一个轴)
t1 = np.arange(12)
print(type(t1))
print(t1)
print(t1.shape)

# 二维数组，两个方向(两个轴)
t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2)
print(t2.shape)

# 三维数组，三个方向(三个轴)
t3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t3)
print(t3.shape)

# shape输出结果有几个元素就代表几维数组，即shape元组的长度即维度
# shape三维数组输出结果:(2, 2, 3),2个块，每个块2行3列
# shape二维数组输出结果:(2, 3),只有一个块，2行3列
# shape一维数组输出结果:(12, ),只有一个块一行，12列
# 如果写(1,12)就是一个二维数组了，出来的数据会多一个中括号

# ndim直接查看数组的维度
print(t1.ndim)
print(t2.ndim)
print(t3.ndim)





