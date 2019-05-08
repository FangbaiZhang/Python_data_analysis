import numpy as np

a = np.random.rand(3, 3)
print(a)
print("*" * 50)

# 指定轴参数排序，列排序, 默认小到大
b = np.sort(a, axis=0)
print(b)