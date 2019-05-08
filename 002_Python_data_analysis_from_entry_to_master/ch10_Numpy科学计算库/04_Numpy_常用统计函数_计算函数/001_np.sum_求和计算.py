# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
print("*" * 50)

# 所有元素求和的值
b = np.sum(a)
print(b)
print("*" * 50)

# 可以传入轴参数，传入轴0即行，每行的对应的每个元素相加，实际就是求的每列的和
c = np.sum(a, axis=0)
print(c)
# 也可以写成以下方式
print(a.sum(axis=0))
print("*" * 50)


# 传入轴1
d = np.sum(a, axis=1)
print(d)
print("*" * 50)


# 任何数字与nan相加的结果还是nan
e = a.astype(float)
e[1, 1] = np.nan
print(e)
print("*" * 50)

f = np.sum(e, axis=0)
print(f)


