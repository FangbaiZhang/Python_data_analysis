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

# 生成标准正态分布的随机浮点数，可以传入浮点数的个数
c = np.random.randn(10)
print(c)
print("*" * 50)

# 生成随机整数，参数上限和下限，生成的个数
d = np.random.randint(-10, 10, 10)
print(d)
print("*" * 50)
