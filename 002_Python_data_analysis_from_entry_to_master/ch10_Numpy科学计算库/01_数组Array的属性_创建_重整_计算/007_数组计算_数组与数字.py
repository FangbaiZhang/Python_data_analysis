# -*- coding:utf-8 -*-
# 数组计算，数组中每个值都会被计算

import numpy as np

# 生成一个一维数组
t1 = np.arange(12)
# 重写成二维数组
t2 = t1.reshape((3, 4))
# 上面可以简写为
# t2 = np.arange(12).reshape((3, 4))
print(t2)

# 乘法
t3 = t2 * 2
print()
print(t3)

# 除法，除以O，python中除以0会报错，
# 数组可以计算出结果,不会报错，会出现警告
t4 = t2 / 0
print()
print(t4)
# 输出结果：0/0=nan(not a number，不是一个数字)   2/0=inf(infinity 无限，无穷大)