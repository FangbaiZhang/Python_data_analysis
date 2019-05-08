# 生成数组常用函数
# Page178

import numpy as np

# zeros生成元素全为0的数组,参数为数组的shape,还可以传入dtype
t1 = np.zeros((1, 3, 3), dtype=int)
print(t1.shape)
print(t1)

t2 = np.zeros((3,))
print(t2)

# ones函数和zeros函数用法相同，不过生成的都是1
t3 = np.ones((1, 3, 3), dtype=int)
print(t3)

# empty函数生成的元素完全是随机的,每运行一次，值都会发生变化
t4 = np.empty((1, 3, 3), dtype=int)
print(t4)