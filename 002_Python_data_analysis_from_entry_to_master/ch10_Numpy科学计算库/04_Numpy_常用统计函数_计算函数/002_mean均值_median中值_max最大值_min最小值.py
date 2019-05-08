# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
print("*" * 50)

# 求均值,求每一列的平均值
# axis=0作用于列
print(a.mean(axis=0))
print("*" * 50)

# 求中值,采用上面mean写法错误，要采用np.median写法
print(np.median(a, axis=0))
print("*" * 50)

# 最大值，最小值，列上的
print(a.max(axis=0))
print(a.min(axis=0))
