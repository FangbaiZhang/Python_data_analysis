# -*- coding:utf-8 -*-

import pandas as pd

# 读取CSV文件
df = pd.read_csv('./dogNames2.csv')
print(df)
# 读取后会自动添加一列索引,从0开始

# read_还有很多方法，json，excel，html等

