# -*- coding:utf-8 -*-

import pandas as pd
from pymongo import MongoClient

# 不传host和port,读取是本地有的数据，打开MongoDB数据库服务
# 管理员运行CMD，然后启动MongoDB，这样就可以读取本地MongoDB里面的所有数据
# 也可以传入服务员端口，读取服务器上的数据
# - 启动MongoDB服务 net start MongoDB 管理员打开CMD窗口
# - 关闭MongoDB服务 net stop MongoDB

# 先连接MongoDB，然后取出数据
# 查找数据库DB(yunqi)中的TABLE(bookInfo)数据转换为列表
client = MongoClient()
collection = client['yunqi']['bookInfo']
data = list(collection.find())

# 数据是一个列表，内部都是字典
print(data[0:2])
print('*' * 100)


# 读取全部数据
t = pd.DataFrame(data)

# 显示头几行，或者末几行，下面读取头两行和末两行
print(t.head(2))
print('*' * 100)
print(t.tail(2))
print('*' * 100)

# 显示
print(t.info())
print(t.describe())
