# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(24).reshape(4, 6)
print(a)
print("*" * 50)

# 修改某几列的数值，将第三列全部修改为0
a[:, 2:3] = 0
print(a)
print("*" * 50)

# 查看布尔值，根据布尔值进行替换
# 把小于10的全部替换为1
print(a < 10)
print("*" * 50)

a[a <10] = 1
print(a)
