# 指定参数为python兼容的bool类型
# 然后调整为int类型

import numpy as np
import random

t5 = np.array([1, 0, 1, 0, 1, 1], dtype=bool)
print(t5)
print(t5.dtype)

# 调整类型
t6 = t5.astype('int32')
print(t6)
print(t6.dtype)

# 生成10个小数的一维数组,random.random()用于生成一个随机小数
# 此处对的random.random()就相当于i, i for i in range(10)
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

# 将t7小数位数保留2为小数点
t8 = np.round(t7, 2)
print(t8)
print(t8.dtype)