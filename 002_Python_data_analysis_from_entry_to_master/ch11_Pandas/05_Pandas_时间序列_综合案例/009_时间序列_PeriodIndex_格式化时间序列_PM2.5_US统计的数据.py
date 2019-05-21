# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 打开911文件
filepath = './PM2.5/BeijingPM20100101_20151231.csv'
df = pd.read_csv(filepath)

# 第一步: 设置时间序列索引
# PeriodIndex用于格式化时间序列,按小时生成时间序列
# 把分开的时间字符串转换为Pandas转换为Pandas的时间序列类型
period = pd.PeriodIndex(year=df['year'], month=df['month'], day=df['day'], hour=df['hour'], freq='H')

# 首先：将上面的时间序列加入到df数组中，设置为一个列索引
df['datetime'] = period

# 然后：将上面的datetime列索引设置为index索引(行索引）
df.set_index('datetime', inplace=True)
print(df.head(3))
print(df.columns)
print('*' * 100)

# 由于数据量太多，绘图数据可以只取部分数据，上面添加时间序列的数据进行降采样
# 求每天的平均值，如果值为NaN,会自动排除掉
df = df.resample('7D').mean()


# 第二步:处理缺失数据
# 处理缺失数据，查看原始数据，有些监测点的PM是NaN
print(df['PM_US Post'])
print('*' * 100)
# 删除缺失的数据,由于是只有一列，不需要指定轴向axis
data = df['PM_US Post'].dropna()
print(data)
print(type(data))
print('*' * 100)


# 第三步：绘图
_x = data.index
# 格式化X轴坐标格式
_x = [i.strftime('%Y-%m-%d') for i in _x]
_y = data.values

plt.figure(figsize=(20, 8), dpi=128)
plt.plot(range(len(_x)), _y)

# 原始画图数据太多，X轴每隔10个填入坐标数据
plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)

plt.show()
