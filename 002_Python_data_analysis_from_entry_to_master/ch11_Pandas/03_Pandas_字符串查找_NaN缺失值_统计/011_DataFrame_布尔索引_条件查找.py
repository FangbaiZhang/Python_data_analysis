# -*- coding:utf-8 -*-

import pandas as pd

# 读取CSV文件，读取后会自动添加一列索引,从0开始
df = pd.read_csv('./dogNames22.csv')
print('*' * 100)

# 按单个条件筛选，挑选出数量大于800的内容
print(df[df['Count_AnimalName'] > 800])
print('*' * 100)

# 按多个条件筛选，使用&符号
print(df[(df['Count_AnimalName'] > 800) & (df['Count_AnimalName'] < 1000)])
print('*' * 100)

# 字符串长度筛选
print(df[(df['Row_Labels'].str.len() > 4) & (df['Count_AnimalName'] > 800)])
print('*' * 100)
