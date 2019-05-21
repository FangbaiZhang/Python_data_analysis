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
# 第一部分内容为报警类型，后面是具体的事项描述,然后转换为列表
temp_list = df['title'].str.split(': ').tolist()
# 提取出小列表中的第一个元素，即分类标签名称
cate_list = [i[0] for i in temp_list]
# 将cate_list列表转换为一个数组
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)), columns=['cate'])
print(cate_df)

# 将数组添加一列分类cate一列
# 将上面的cate_df数组添加到df数组中
# 合并数组，原数组不变
# print(df.join(cate_df))

# 直接赋值，原数组改变
df['cate'] = cate_df
print(df.head(5))

# 按cate进行分组，统计每组包含的数据，然后只取title该列
print(df.groupby(by='cate').count()['title'])


# 案例001和002都是使用前面的分组聚合方法，进行数据处理
# 对于数据中有时间相关索引的可以使用时间序列，更加方便简洁
# 参考之后的案例