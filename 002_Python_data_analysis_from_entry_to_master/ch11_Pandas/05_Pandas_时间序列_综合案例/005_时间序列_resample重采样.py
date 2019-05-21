# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 重采样：指的是将时间序列从一个频率转化为另一个频率进行处理的过程，
# 将高频率数据转化为低频率数据为降采样，低频率转化为高频率为升采样
# pandas提供了一个resample的方法来帮助我们实现频率转化

# 创建一个时间序列数组
# numpy.random.uniform(low,high,size)
# 从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high
t = pd.DataFrame(np.random.uniform(10, 50, (100, 1)), index=pd.date_range('20170101', periods=100))
print(t)
print('*' * 100)

# 上面是按天进行索引的
# 降采样，按照月进行统计,并求每月的平均值，得到一个新的数组
t1 = t.resample('M').mean()
print(t1)
print('*' * 100)

# 降采样，按照10天进行统计,并求每月的平均值，得到一个新的数组
t1 = t.resample('10D').mean()
print(t1)
print('*' * 100)

# 降采样，按照10天进行统计,并求10天的和，得到一个新的数组
t1 = t.resample('10D').sum()
print(t1)
print('*' * 100)

# 降采样，按照10天进行统计,统计个数，得到一个新的数组
t1 = t.resample('10D').count()
print(t1)
print('*' * 100)
