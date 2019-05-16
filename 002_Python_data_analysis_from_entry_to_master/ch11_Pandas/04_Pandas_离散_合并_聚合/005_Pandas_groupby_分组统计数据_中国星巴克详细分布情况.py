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

# 先提取出中国的数据,结果是一个DataFrame
china_data = df[df['Country'] == 'CN']
# print(china_data)

# 统计每一个省份里面星巴克的数量，但是该处的by索引省份不是具体名称，而是数字代号
grouped = china_data.groupby(by='State/Province')
province_count = grouped['Brand'].count()
print(province_count)
print(type(province_count))



