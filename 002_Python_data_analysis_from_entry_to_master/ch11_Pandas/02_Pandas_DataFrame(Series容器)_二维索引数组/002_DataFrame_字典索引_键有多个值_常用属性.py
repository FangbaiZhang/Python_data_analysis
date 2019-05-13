# -*- coding:utf-8 -*-

import pandas as pd

# 方式1:直接传入字典
d1 = {'name': ['xiaohong', 'xiaoming'], 'age': ['20', '25'], 'Tel': ['10010', '10086']}
d2 = pd.DataFrame(d1)
print(d2)
print(type(d2))
print('*' * 100)

# 字典创建索引，键作为columns列索引，index行索引默认为0开始的数组

# 方式2：传入字典组成的列表,如果有缺失的值，就是Nan
d3 = [{'name': 'xiaohong', 'age': 20, 'Tel': '10010'}, {'name': 'xiaoming', 'Tel': '10086'}]
d4 = pd.DataFrame(d3)
print(d4)
print('*' * 100)

# DataFrame的常用属性查看
print(d4.index)
print(d4.columns)
print(d4.shape)
print(d4.size)
