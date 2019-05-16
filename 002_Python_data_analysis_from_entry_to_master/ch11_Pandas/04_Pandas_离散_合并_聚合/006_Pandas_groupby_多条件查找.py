# -*- coding:utf-8 -*-

import pandas as pd


# 打开星巴克文件
filepath = './starbucks_store_worldwide.csv'
df = pd.read_csv(filepath)

# 多条件查找方式1：结果是Series
# 多条件查找，只取一部分数据,以下方式由于是先固定了Country一列，然后里面在分组数据，结果是一个Series一维数组
print("方式1的Series结果:")
df1 = df['Country'].groupby(by=[df['Country'], df['State/Province']])
print(df1)
# 统计每个国家每个省份下星巴克的数量，但是结果其实是一个Series
print(type(df1.count()))
print(df1.count())
print('*' * 100)

# 多条件查找方式2：结果是DataFrame
# 先提取出所有国家的DataFrame，然后按国家和省份两个条件进行分组
print("方式2的DataFrame结果:")
df2 = df[['Country']].groupby(by=[df['Country'], df['State/Province']])
print(df2)
print("方式2的复合索引结构:")
print(df2.count().index)
print('*' * 100)
print("方式2的复合索引数据结果:")
print(df2.count())
print('*' * 100)

# 多条件查找方式3：结果是DataFrame,这种写法和上面方式2结果一样
# 但是输出结果最后一列上面有个Country索引
print("方式3的DataFrame结果:")
df3 = df.groupby(by=['Country', 'State/Province'])[['Country']].count()
print(df3)

# 上面方式2和方式3的结果相同，输出结果的前两列都是索引
# 因为上面分组by里面传入了两个条件，复合索引MultiIndex





