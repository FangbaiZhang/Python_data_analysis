# -*- coding:utf-8 -*-
import numpy as np

# nan的一些特性
# 两个nan是不相等的
print(np.nan == np.nan)
print(np.nan != np.nan)
print("*" * 50)

# 创建一个浮点型数组,并修改其中一个值为nan
a = np.arange(24, dtype=float).reshape(4, 6)
a[3, 3] = np.nan
print(a)
print("*" * 50)

# 统计数组中不为0的个数,先将第一列全部修改为0
a[:, 0] = 0
print(a)
print(np.count_nonzero(a))
print("*" * 50)

# 利用nan不相等的特性，只有nan元素处为True=1,False=0
print(a != a)
# 因此，可以利用这一个nan这个特性，采用以下找不等于0的方式统计nan的值
print(np.count_nonzero(a != a))
print("*" * 50)

# isnan判断里面的值是不是nan，结果和上面一样
print(np.isnan(a))
print(np.count_nonzero(np.isnan(a)))
print("*" * 50)