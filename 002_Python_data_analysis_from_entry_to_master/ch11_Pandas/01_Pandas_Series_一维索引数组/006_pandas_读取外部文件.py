# -*- coding:utf-8 -*-

import pandas as pd

# 读取CSV文件
# 默认使用第一行作为header标签索引，
# 如果header=None,则自动使用数字作为索引
# 也可以使用names传入自定义标签索引
df = pd.read_csv('./dogNames2.csv')
print(df)
# 读取后会自动添加一列索引,从0开始

# read_还有很多方法，json，excel，html等

