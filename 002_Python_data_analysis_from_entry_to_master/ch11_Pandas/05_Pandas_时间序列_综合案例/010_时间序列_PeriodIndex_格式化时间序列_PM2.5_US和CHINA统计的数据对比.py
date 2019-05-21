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

# 上面提取的是US统计的数据，下面我们提取CHINA统计的数据，绘制到同一张图上
data_china = df['PM_Dongsi'].dropna()
print(data_china)
print('*' * 100)

# china2013年之前的数据都没有
# 由于缺失的数据不一样，两个数据的长度不一样
# 为了保持绘图数据一致,直接使用时间作为横坐标，这样数据才能对应一致

# 第三步：绘图
_x = data.index
# 格式化X轴坐标格式
_x = [i.strftime('%Y-%m-%d') for i in _x]
_y = data.values

_x_china = data_china.index
_x_china = [i.strftime('%Y-%m-%d') for i in _x_china]
_y_china = data_china.values

plt.figure(figsize=(20, 8), dpi=128)
plt.plot(_x, _y, label='PM_US Post')
plt.plot(_x_china, _y_china, label='PM_Dongsi')

# 原始画图数据太多，X轴每隔10个填入坐标数据
plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
# 显示图例名称，位置最佳位置
plt.legend(loc='best')
# 由于2013-01-25前面的数据中国没有，我们可以设置X轴坐标
# 由于是日期，设置时候需要加上引号
# 注意，起始日期必须是2013-01-25，多一天少一天图形没有显示，结束日期不影响
plt.xlim('2013-01-25', '2015-12-15')


plt.show()
