# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 打开911文件
filepath = './911.csv'
df = pd.read_csv(filepath)
print(df.head(5))
print('*' * 100)

# 将时间字符串一列转换为pd里面的时间序列
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# 然后将timeStamp这一列设置为行索引，替换掉原来的数字索引,替换后行是一个复合索引
df.set_index('timeStamp', inplace=True)
print(df.head(5))
print('*' * 100)

# 重新按月份采样,然后统计每个月的数量,取出title这一列即可，结果是一个一维数组
count_by_month = df.resample('M').count()['title']
print(count_by_month)
print(type(count_by_month))
print('*' * 100)


# 画图展示
# 由于时间索引后面有时间00:00:00我们需要格式化去掉
_x = count_by_month.index
# 格式化上面的时间标签
_x = [i.strftime('%Y-%m-%d') for i in _x]
print(_x)
_y = count_by_month.values

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=128)

# 传入绘图数据
plt.plot(range(len(_x)), _y)
# 将X轴和时间序列标签一一对应
plt.xticks(range(len(_x)), _x, rotation=45)

plt.show()



