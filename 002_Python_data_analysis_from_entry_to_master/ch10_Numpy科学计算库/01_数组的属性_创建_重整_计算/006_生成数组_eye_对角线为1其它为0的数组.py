# -*- coding:utf-8 -*-

import numpy as np

# 参数为对角线有几个1,生成的就是一个正方形二维数组
a = np.eye(5)
print(a)
print("*" * 50)

# 将1全部替换为-1
a[a ==1 ] = -1
print(a)