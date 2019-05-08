# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(24).reshape(4, 6)
print(a)
print("*" * 50)

# clip可以满足两个条件的运算
# clip(10, 18)小于10的替换为10,大于18的替换为18
b = a.clip(10, 18)
print(b)
print("*" * 50)



