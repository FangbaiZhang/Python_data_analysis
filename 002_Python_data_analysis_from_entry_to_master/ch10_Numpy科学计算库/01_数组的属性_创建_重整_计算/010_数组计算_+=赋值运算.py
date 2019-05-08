# -*- coding:utf-8 -*-
# Page185
import numpy as np


# 数组中有 += /= 运算符，这里运算符不会生成一个新数组，而是直接对原来的数组的元素的值进行修改
t1 = np.ones((3, 3), dtype='int32')
print(t1)
t1 += 1
print(t1)