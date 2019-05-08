# -*- coding:utf-8 -*-

import numpy as np

# 生成随机整数，参数上限和下限，形状
a = np.random.randint(10, 20, (4, 4))
print(a)
print("*" * 50)

# 生成标准分布的浮点数，传入形状，标准差为1
b = np.random.randn(4, 4)
print(b)
print("*" * 50)