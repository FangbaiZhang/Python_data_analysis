# -*- coding:utf-8 -*-
# Page179

import numpy as np
import random

# arange生成一维数组，可以传入三个参数，起始终止和步长，默认起始为0，步长为1
t1 = np.arange(0, 6, 2, dtype=int)
print(t1)
print("**************************************************")

# rand函数生成元素在[0, 1)区间均匀分布的浮点数数组，传入参数为shape
t2 = np.random.rand(2, 3, 3)
print(t2)

# random生成随机的浮点数
t3 = np.array([random.random() for i in range(5)])
print("**************************************************")
print(t3)
