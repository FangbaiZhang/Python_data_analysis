# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建一个二维索引数组
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('WXYZ'))
print(t3)
print(type(t3))
print('*' * 100)

# 通过行列索引取出交叉点的值
print(t3.loc['a', 'Z'])
print('*' * 100)

# 取指定行列，还是可以采用007中的切片索引方式，数字和字符串结合使用
t2= t3[0:1]
print(t2)
print(type(t2))
print('*' * 100)

# 取指定行
t4 = t3.loc['a']
print(t4)
print(type(t4))
print('*' * 100)

# 注意采用loc和切片方式只取出一行的的结果类型不一样
# 切片取出来的还是二维索引数组，loc取出来是Series一维数组了

