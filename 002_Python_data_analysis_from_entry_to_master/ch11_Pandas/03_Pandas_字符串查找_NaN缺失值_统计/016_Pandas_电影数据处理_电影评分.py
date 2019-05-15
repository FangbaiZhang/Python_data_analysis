# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 共有1000部电影的数据
filepath = './IMDB-Movie-Data.csv'
df = pd.read_csv(filepath)

# 读取前三行，查看结构，查看概览信息
print(df.head(3))
print(df.info())
print('*' * 100)

# 提取电影评分数据，转换为列表
rating_data = df['Rating'].values.tolist()
print(rating_data)
# 平均评分
print(df['Rating'].mean())

# 提取导演数据,统计导演人数
print(len(df['Director'].unique()))

# 获取演员的人数，一部电影的演员有多个，逗号连接的，先以逗号进行分割为一个列表
actor = df['Actors'].str.split(',')
# 将所有数据生成一个列表
actors = actor.tolist()
# print(actor)
# print(actors)

# 转换为一位数组,然后转化为列表
actors_list = list(np.array(actors).flatten())
print(actors_list)