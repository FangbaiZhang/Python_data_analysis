# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 用来正常显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 使用matplotlib展示中国星巴克分布情况
# 打开星巴克文件
filepath = './starbucks_store_worldwide.csv'
df = pd.read_csv(filepath)
# 提取出属于中国的DataFrame数据
df = df[df['Country'] == 'CN']

# 提取省份数据
# 按国家分组，统计出每个国家的星巴克数量，Brand里面没有缺失数据，按这个索引统计数量
data1 = df.groupby(by='City')['Brand'].count()
print(data1)
print('*' * 100)
# 按数量降序排列，取前十名的数据
data2 = data1.sort_values(ascending=False)[0:20]
print(data2)
print(type(data2))
print('*' * 100)

# 绘图，提取结果是一个Series一维数据，直接提取index和值
_x = data2.index
_y = data2.values

plt.figure(figsize=(20, 8), dpi=128)

# 绘制柱状图
# 可以直接绘制
# plt.bar(_x, _y)

# x坐标用数字对应字符串，可以方便调整X轴的刻度大小和柱子的宽度
plt.bar(range(len(_x)), _y, width=0.3, color='#B3A9FF')
# 坐标轴数字转换为字符串城市名称
plt.xticks(range(len(_x)), _x)

plt.show()
