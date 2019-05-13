# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建一个二维数组
t1 = np.arange(12).reshape(3, 4)
print(t1)
print('*' * 100)

# 创建二维索引数组，添加行索引和列索引
t2 = pd.DataFrame(t1)
print(t2)
print('*' * 100)

# 竖向第一列，是index,行的索引, axis=0
# 横向第一行，是columns,列的索引, axis=1

# 我们可以指定行列索引的名称,传入的索引是一个列表
t3 = pd.DataFrame(t1, index=list('abc'), columns=list('1234'))
print(t3)