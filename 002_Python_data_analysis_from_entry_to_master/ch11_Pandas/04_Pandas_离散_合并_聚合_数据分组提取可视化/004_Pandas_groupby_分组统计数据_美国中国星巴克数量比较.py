# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 打开星巴克文件
filepath = './starbucks_store_worldwide.csv'
df = pd.read_csv(filepath)


# 查看基本信息
print(df.head(3))
print('*' * 100)
print(df.info())
print('*' * 100)

# 选取出美国的数据
# print(df[df['Country'] == 'US'])
# 按国家进行分组，分组后的结果是每个国家一个单独的元组

# grouped是一个DataFrame对象，是可迭代的，其中每一个元素是一个元组
# 元组里面就是by索引分组后的值（分组之后的一个DataFrame）
grouped = df.groupby(by='Country')
print(grouped)

# 分组后的对象可以进行遍历操作，调用聚合方法，分组的后的数据是DataFrame数据,先转换为列表，查看前两个元素
for i in list(grouped)[0:2]:
    print(i) # 看下每个i是什么
    print('*' * 100)
# 输出结果显示，每个国家分为一个组，放在一个元组里面，元组里面第一个元素就是国家代码，之后有一个DataFrame数据

# 统计没有缺失数据的'Brand'一列的数据，即统计了每个国家星巴克的数量
# 这样统计出来的结果是一个Series数组
country_count = grouped['Brand'].count()
print(country_count)
print(type(country_count))
print('*' * 100)

# 提取美国和中国星巴克的数量
print(country_count['US'])
print(country_count['CN'])

