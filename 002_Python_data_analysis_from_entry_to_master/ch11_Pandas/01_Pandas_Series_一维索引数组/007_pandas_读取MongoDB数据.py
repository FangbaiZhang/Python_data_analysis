# -*- coding:utf-8 -*-

import pandas as pd
from pymongo import MongoClient

# 不传host和port,读取是本地有的数据，打开MongoDB数据库服务
# 管理员运行CMD，然后启动MongoDB，这样就可以读取本地MongoDB里面的所有数据
# 也可以传入服务员端口，读取服务器上的数据
# - 启动MongoDB服务 net start MongoDB 管理员打开CMD窗口
# - 关闭MongoDB服务 net stop MongoDB

# 先连接MongoDB，然后取出数据
client = MongoClient()
collection = client['yunqi']['bookInfo']
# 查找数据转换为列表
data = list(collection.find())

# 数据是一个列表，内部都是字典
print(data[0:2])
print('*' * 100)

# 读取数据，每个字典当做一个元素，当做一行读取出来，添加索引
t1 = data[0:2]
t1 = pd.Series(t1)
print(t1)
print('*' * 100)

# 读取出字典中的内容，键是索引，值是值
t2 = data[0]
t2 = pd.Series(t2)
print(t2)
print('*' * 100)