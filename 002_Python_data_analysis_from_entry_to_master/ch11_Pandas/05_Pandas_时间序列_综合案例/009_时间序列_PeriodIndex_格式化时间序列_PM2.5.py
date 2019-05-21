# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 打开911文件
filepath = './PM2.5/BeijingPM20100101_20151231.csv'
df = pd.read_csv(filepath)

# PeriodIndex用于格式化时间序列,按小时生成时间序列
# 把分开的时间字符串转换为Pandas转换为Pandas的时间序列类型
period = pd.PeriodIndex(year=df['year'], month=df['month'], day=df['day'], hour=df['hour'], freq='H')

# 首先：将上面的时间序列加入到df数组中，设置为一个列索引
df['datetime'] = period

# 然后：将上面的datetime列索引设置为index索引(行索引）
df.set_index('datetime', inplace=True)
print(df.head(3))
print('*' * 100)
