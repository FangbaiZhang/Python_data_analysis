# -*- coding:utf-8 -*-
import numpy as np

# nan(NAN,Nan):not a number表示不是一个数字
# 什么时候numpy中会出现nan：
# 当我们读取本地的文件为float的时候，如果有缺失，就会出现nan
# 当做了一个不合适的计算的时候(比如无穷大(inf)减去无穷大)
# 任何数字与nan相加的结果还是nan

# inf(-inf,inf):infinity,inf表示正无穷，-inf表示负无穷
# 什么时候回出现inf包括（-inf，+inf）
# 比如一个数字除以0，（python中直接会报错，numpy中是一个inf或者-inf）

a = np.arange(24).reshape(4, 6)
print(a)
print("*" * 50)

# 将数值修改为nan或inf,nan和inf是浮点类型，首先需要将数据类型转换为浮点型
b = a.astype(float)
print(b)
print("*" * 50)

# 修改数值为nan
b[1] = np.nan
print(b)

