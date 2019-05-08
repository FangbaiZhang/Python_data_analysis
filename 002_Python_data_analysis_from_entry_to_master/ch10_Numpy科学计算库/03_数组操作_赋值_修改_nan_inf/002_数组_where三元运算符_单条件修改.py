# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(24).reshape(4, 6)
print(a)
print("*" * 50)

# where三元运算符:满足某一个条件进行操作
# where(a<10, 0, 100)
# 将a中小于10的全部替换为10，大于等于10的全部替换为100
b = np.where(a<10, 0, 100)
print(b)
print("*" * 50)