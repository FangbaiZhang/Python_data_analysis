# -*- coding:utf-8 -*-

import pandas as pd

# 读取CSV文件，读取后会自动添加一列索引,从0开始
# 生成的是一个二维维数组
df = pd.read_csv('./dogNames22.csv')
print(df.ndim)
print(df.shape)
print('*' * 100)

# 取行，取列注意事项：
# 方括号中直接写数字，表示取行，对行进行操作
# 方括号中写字符串，表示取列，对列进行操作

# 取连续的几列，类似列表切片
print(df[8:10])
print('*' * 100)

# 取每一列，写列索引的字符串，左边第一列的索引会同时取出
# 取了某一列后又可以只取里面的几行
print(df['Row_Labels'][8:10])
print('*' * 100)

# 同时取几行对应的某几列，连着写即可
print(df[8:10]['Row_Labels'])
print('*' * 100)

# 上面两种方式取出的结果一样

