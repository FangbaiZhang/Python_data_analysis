# -*- coding:utf-8 -*-

import pandas as pd

# 读取CSV文件，读取后会自动添加一列索引,从0开始
df = pd.read_csv('./dogNames22.csv')
print(df)
print('*' * 100)

# 对指定条件的值或者索引进行排序
# 默认小到大，False从大到小
df = df.sort_values(by='Count_AnimalName', ascending=False)
print(df)
