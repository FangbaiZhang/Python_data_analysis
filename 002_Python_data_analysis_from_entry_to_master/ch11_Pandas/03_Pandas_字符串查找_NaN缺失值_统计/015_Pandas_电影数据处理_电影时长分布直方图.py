# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 共有1000部电影的数据
filepath = './IMDB-Movie-Data.csv'
df = pd.read_csv(filepath)

# 读取前三行，查看结构，查看概览信息
print(df.head(3))
print(df.info())
print('*' * 100)

# 统计rating,runtime分布情况
# 提取数据
runtime_data = df['Runtime (Minutes)'].values
# print(list(runtime_data))
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 根据电影时间计算分组，分成10组，计算组距
num_bin = (max_runtime - min_runtime) // 10

# 开始绘图
plt.figure(figsize=(20, 8), dpi=128)

# 绘制直方图
plt.hist(runtime_data, num_bin)
# 设置刻度
plt.xticks(range(min_runtime, max_runtime + 5, 5))

plt.show()
