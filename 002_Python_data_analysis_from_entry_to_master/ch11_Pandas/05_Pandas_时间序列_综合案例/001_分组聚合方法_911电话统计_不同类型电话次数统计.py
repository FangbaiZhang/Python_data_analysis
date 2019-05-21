# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 打开911文件
filepath = './911.csv'
df = pd.read_csv(filepath)

# 查看基本信息和每行的具体内容
# print(df.head(3))
# print(list(df.iloc[5]))
print('*' * 100)
print(df.info())
print('*' * 100)

# 查看基本信息，分类放在title里面
# 获取分类的情况,转换为字符串，然后用从： 出进行分割为前后两部分内容
# 第一部分内容为报警类型，后面是具体的事项描述
df1 = df['title'].str.split(': ')
# print(df1)
# 上面的df1一维数组转换为列表
df2 = df1.tolist()
# print(df2)


# 统计分类信息，提取上面列表子列表中的第一个元素(分类名称),使用set去重
cate_list = list(set([i[0] for i in df2]))
print(cate_list)
print('*' * 100)

# 构造全为0的数组，行数和df相同，列数就是分类的标签，列标签就是分类的标签
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
# print(zero_df)
print('*' * 100)

# 赋值，df中包含该分类的时候进行赋值为1，
# 遍历三个分类，通过布尔值为True选定后赋值
for cate in cate_list:
    # 查看一个分类中的title的字符串中是否包含该分类名称
    # 使用布尔索引，比如先查看zero_df的Fire分类，Fire这一列，
    # 再查看df的title这一列，是否包含该分类，包含的话结果就是True
    # 布尔索引为True,则zero_df该列的对应的该行就可以被选定，然后可以将其赋值为1
    # print(zero_df[cate][df['title'].str.contains(cate)])
    # [df['title'].str.contains(cate)]的结果是True或者False
    zero_df[cate][df['title'].str.contains(cate)] = 1

print(zero_df)
print('*' * 100)

# 对列进行求和操作，统计出每个分类下的总个数
cate_sum = zero_df.sum(axis=0)
print(cate_sum)