# -*- coding:utf-8 -*-
# pandas创建Series创建index索引

import pandas as pd
import numpy as np
import string


# string.ascii_uppercase可以生成ascii值，字母
t1 = pd.Series(np.arange(10), index=list(string.ascii_uppercase[:10]))
print(t1)


# 创建一个字典，然后转换为数组索引
print(string.ascii_uppercase[0:5])
print(string.ascii_lowercase[0:5])
a = {string.ascii_uppercase[i]:i for i in range(10)}
print(a)

# 字典转换为索引数组
b = pd.Series(a)
print(b)

# 查看维度和形状
print(b.ndim)
print(b.shape)
