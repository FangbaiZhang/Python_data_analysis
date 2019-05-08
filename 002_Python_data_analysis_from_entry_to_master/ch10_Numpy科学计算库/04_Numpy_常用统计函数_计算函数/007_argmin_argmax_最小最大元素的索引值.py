# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(12, dtype=int).reshape(4, 3)
print(a)
print("*" * 50)

# 最小元素的索引值,不指定参数，则先将数组自动转换为一维数组
print(a.argmin())
# 最大元素的索引值
print(a.argmax())
print("*" * 50)

# 可以指定轴向,axis=0，作用于列，找出每列最大元素的位置
print(a.argmax(axis=0))
# axis=1，作用于行，找出每行最大元素的位置
print(a.argmax(axis=1))