# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建一个时间序列，不传参数默认
time_index = pd.date_range('20170101', periods=10, freq='D')
print(time_index)
print('*' * 100)

# 创建一个数组，使用上面的时间序列作为行标签索引
df = pd.DataFrame(np.random.rand(10), index=time_index)
print(df)
print('*' * 100)