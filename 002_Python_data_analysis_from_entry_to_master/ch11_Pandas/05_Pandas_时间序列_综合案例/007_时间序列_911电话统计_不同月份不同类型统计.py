# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 打开911文件
filepath = './911.csv'
df = pd.read_csv(filepath)
print(df.head(5))
print(df.index)
print('*' * 100)

# 注意，第一步和第二步不能颠倒，先进行添加分类索引，然后再添加时间序列
# 可以通过查看索引的具体结构，如果先添加时间序列索引，索引的结构就改变了
# 再设置标签索引，会通过时间索引找对应的值，但是分类索引的行索引没有相应的时间索引
# 最后结果就是分类索引该列的值全部是NaN

# 第一步：添加分类一列
# 原数组进行分类，最终添加一列分类标签索引
# 查看基本信息，分类放在title里面
# 获取分类的情况,转换为字符串，然后用从： 出进行分割为前后两部分内容
# 第一部分内容为报警类型，后面是具体的事项描述,然后转换为列表
temp_list = df['title'].str.split(': ').tolist()
# 提取出小列表中的第一个元素，即分类标签名称
cate_list = [i[0] for i in temp_list]
# 将cate_list列表转换为一个数组
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)), columns=['cate'])
# 直接赋值，原数组改变，添加了cate一列
df['cate'] = cate_df
print(df.head(5))
print(df.index)
print('*' * 100)

# 第二步：添加时间序列
# 将时间字符串一列转换为pd里面的时间序列
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# 然后将timeStamp这一列设置为行索引，替换掉原来的数字索引,替换后行是一个复合索引
df.set_index('timeStamp', inplace=True)
print(df.head(5))
print(df.index)
print('*' * 100)

# 第三步：分类统计，然后绘图
# 设置一个图形
plt.figure(figsize=(20, 8), dpi=128)

# 循环三次,将三个分类画在一个图形上面
for group_name, group_data in df.groupby(by='cate'):
    # 分类后按月进行统计
    count_by_month = group_data.resample('M').count()['title']

    _x = count_by_month.index
    _x = [i.strftime('%Y-%m-%d') for i in _x]
    _y = count_by_month.values

    plt.plot(range(len(_x)), _y, label = group_name)
    plt.xticks(range(len(_x)), _x, rotation=45)


plt.legend(loc='best')
plt.show()

