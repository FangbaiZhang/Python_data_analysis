# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 共有1000部电影的数据
filepath = './IMDB-Movie-Data.csv'
df = pd.read_csv(filepath)

# 查看电影分类信息
print(df['Genre'].head(3))
print('*' * 100)

# 一部电影属于多个分类，统计每个分类下电影的数量
# 重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1
# 每个分类下的1求和，就是该分类下电影的数量

# 提取出所有电影分类的大列表，列表元素就是每部电影分类的列表
temp_list = df['Genre'].str.split(',').tolist() # 结果[[], ....[], []]
# 将temp_list展开为一个列表，先用j提取出每个小列表，然后i提取小列表中的每个元素，使用set删除列表中的重复元素
genre_list = list(set([i for j in temp_list for i in j]))
# print(genre_list)

# 构造全为0的数组，行数就是df的行数(shape[0]即行数)，索引就是数字，列数就是电影分类的个数，索引就是每个分类的名称
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
print(zeros_df.head(3))

# 每部电影出现分类的地方将0赋值为1,遍历每一行电影
for i in range(df.shape[0]):
    # 比如i=0，先定位到zeros_df数组的第1行
    # temp_list[0]就是上面大列表的第一个元素，就是第一部电影分类的列表
    # zeros_df.loc[0, ['Sci-fi', 'Musical']] = 1
    # 定位到0行，列索引为Sci-fi,Musical元素修改为1
    zeros_df.loc[i, temp_list[i]] = 1

print(zeros_df.head(3))

# 统计每个分类下电影的数量和,对列求和，即对竖向轴0操作
genre_count = zeros_df.sum(axis=0)
# 排序，按电影数量由大到小排序
genre_count = genre_count.sort_values(ascending=False)
print(genre_count)

# 绘制柱状图，列索引是横坐标
_x = genre_count.index
_y = genre_count.values

plt.figure(figsize=(20, 8), dpi=128)
plt.bar(_x, _y)

plt.show()




