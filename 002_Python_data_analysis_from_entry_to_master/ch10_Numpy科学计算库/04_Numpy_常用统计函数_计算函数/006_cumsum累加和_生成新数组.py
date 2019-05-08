# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
print("*" * 50)

# 求列的累加和,列的该元素与前一个元素相加得到本元素，一直前一个加后一个
# 最后得到一个新的数组
d1 = np.cumsum(a, axis=0)
print(d1)
print("*" * 50)

# 求行的累加和
d2 = np.cumsum(a, axis=1)
print(d2)