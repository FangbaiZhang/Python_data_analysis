# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建一个DataFrame
df = pd.DataFrame(np.arange(9).reshape((3, 3)), index=list('ABC'), columns=list('xyz'))
print(df)
print('*' * 100)

# 索引直接赋值修改
df.index= list('abc')
print(df)
print('*' * 100)

# 重新赋值，如果本来有的行，直接复制，没有的添加一行，但是值都是NaN
df1 = df.reindex(list('abe'))
print(df1)
print('*' * 100)

# index是一个可迭代对象，可以求长度，也可以转换为一个list列表

# 打开星巴克文件
filepath = './starbucks_store_worldwide.csv'
df = pd.read_csv(filepath)
df3 = df.groupby(by=['Country', 'State/Province'])[['Country']].count()
print(df3)
print(df3.index)
# index最后输出有一个names=['Country', 'State/Province']
# 就是前两列复合索引最上面的名称

