# -*- coding:utf-8 -*-

# pandas创建Series创建带标签的一维数组

import pandas as pd

# 列表添加索引,索引在左，元素在右
t1 = pd.Series(list(range(5)), index=list('abcde'))
print(t1)

# 字典转换为索引,字典的键就是索引
dict1 = {'a': 1, 'b': 2, 'c': 3}
t2 = pd.Series(dict1)
print(t2)




# 内置的enumerate函数也可以添加索引添加起始下标位置
# 结果为一个元组组成的新列表
new_seasons = list(enumerate(list(range(5)), start=100))
print(new_seasons)