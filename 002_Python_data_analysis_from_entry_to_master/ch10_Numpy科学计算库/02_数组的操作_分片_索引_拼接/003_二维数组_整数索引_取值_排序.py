# -*- coding:utf-8 -*-
# Page190

import numpy as np

# 生成二维数组
a = np.arange(16).reshape(4, 4)
print(a)
print("*" * 50)


# 取出右下角的单个元素的写法
print(a[3, 3])
print(a[3][3])
print("*" * 50)

# 取出所有对角线上的值,第一个列表是行号，第二个列表是列号，元素一一对应
b = a[[0, 1, 2, 3],[0, 1, 2, 3]]
print(b)
print("*" * 50)

# 重新定义各行的行号
# 对二维数组进行排序, 第四行变成第一行，第三行变成第二行
c = a[[3, 2, 1, 0]]
print(c)
