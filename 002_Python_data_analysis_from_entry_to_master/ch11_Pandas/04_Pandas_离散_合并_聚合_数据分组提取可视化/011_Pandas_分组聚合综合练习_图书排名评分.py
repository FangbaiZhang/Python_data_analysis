# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 用来正常显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 打开图书文件
filepath = './books.csv'
df = pd.read_csv(filepath)
print(df.head(2))
print('*' * 100)
print(df.info())
print('*' * 100)
# 输出结果显示有些数据有缺失original_publication_year有些年份没有图书

# 我们要提取出版年份original_publication_year对应的书籍和其平均评分average_rating
# 我们提取出有图书出版的年份的DataFrame数据，删除掉没有出版书籍年份的数据
data1 = df[pd.notnull(df['original_publication_year'])]

# 然后以出版年份对书籍平均评分进行分组
# 也可以对多个索引进行分组，分组后结果就是DataFrame二维数组，可以使用for遍历元素
# grouped = data1[['average_rating', 'original_title']].groupby(by=data1['original_publication_year'])
grouped = data1['average_rating'].groupby(by=data1['original_publication_year'])
# 然后对分组后每年的所有的图书的平均值再求平均值，就是当年出版所有图书的平均评分
# 因为我们只取了一列，最终结果就是一个Series一维数组，如果上面average_rating使用的是两个中括号，结果就是DataFrame结构
grouped = grouped.mean() # 只能对数字使用mean()方法
print(type(grouped))
print(grouped)
print('*' * 100)

# 开始绘图
_x = grouped.index
_y = grouped.values


plt.figure(figsize=(20, 8), dpi=128)
# 出版年份不一定连续，我们出版年份数据和连续的数据一一对应起来
plt.plot(range(len(_x)), _y)
# 年份数据太多，我们将其按10的步长进行分组
# 输出结果X轴是小数，我们将其转换为整数，_x对应的值是索引直接可以使用astype方法
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=45)

# 输出结果显示，较早年份书籍评分波动大，后期波动小
# 前期书籍少，后期书籍多，评价均匀

plt.show()





