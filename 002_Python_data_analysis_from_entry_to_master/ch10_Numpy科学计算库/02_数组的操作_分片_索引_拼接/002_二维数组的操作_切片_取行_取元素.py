# -*- coding:utf-8 -*-
# Page186

# 二维数组是一个矩阵，左上角当做原点(0, 0)
# 行当做x，列当做y，第二行第三列就是(2-1, 3-1)=(1, 2)

import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
print("*" * 50)

# 取出第一行
print(a[0])
print("*" * 50)

# 取出多行,类似列表切片操作
print(a[1:3])
print("*" * 50)

# 取出不连续的多行，使用逗号，外面再加一个中括号即可
print(a[[1, 3]])
print("*" * 50)

# 取出第一个元素和最右下角的15,(4-1, 4-1)=(3, 3)
print(a[0, 0])
print(a[3, 3])
print(type(a[3, 3]))

# 二维数组取值也可以写成以下方式
print(a[3][3])