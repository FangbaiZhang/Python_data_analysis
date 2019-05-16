# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 使用matplotlib展示店铺总数排名前10的国家
# 打开星巴克文件
filepath = './starbucks_store_worldwide.csv'
df = pd.read_csv(filepath)

# 提取数据
# 按国家分组，统计出每个国家的星巴克数量，Brand里面没有缺失数据，按这个索引统计数量
data1 = df.groupby(by='Country')['Brand'].count()
print(data1)
print('*' * 100)
# 按数量降序排列，取前十名的数据
data2 = data1.sort_values(ascending=False)[0:10]
print(data2)
print(type(data2))
print('*' * 100)

# 绘图，提取结果是一个Series一维数据，直接提取index和值
_x = data2.index
_y = data2.values

plt.figure(figsize=(20, 8), dpi=128)

# 绘制柱状图
plt.bar(_x, _y)

plt.show()
