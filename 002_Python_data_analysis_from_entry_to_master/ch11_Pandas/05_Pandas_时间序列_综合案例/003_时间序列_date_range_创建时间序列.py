# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建不同的时间序列DatetimeIndex

# 创建一个时间范围,freq='D'表示频率间隔以天为单位
dr = pd.date_range(start='20171230', end='20180131', freq='D')
print(dr)
print('*' * 100)

dr = pd.date_range(start='20171230', end='20180131', freq='10D')
print(dr)
print('*' * 100)

# 创建一个时间范围,periods=10表示周期为10，freq='D'表示频率间隔以天为单位
dr = pd.date_range(start='20171230', periods=10, freq='D')
print(dr)
print('*' * 100)

# 以月为频率，可以看出每个月多少天
dr = pd.date_range(start='20171230', periods=10, freq='M')
print(dr)
print('*' * 100)


# 以小时为频率
dr = pd.date_range(start='2017/12/30 10:00:00', periods=10, freq='H')
print(dr)
print('*' * 100)