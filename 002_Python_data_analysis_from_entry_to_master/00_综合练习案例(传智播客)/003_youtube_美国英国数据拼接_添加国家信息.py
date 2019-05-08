# -*- coding:utf-8 -*-

import numpy as np

# 创建文件路径
us_data_path = './youtube_video_data/US_video_data_numbers.csv'
uk_data_path = './youtube_video_data/GB_video_data_numbers.csv'

# 加载文件读取为数组形式，delimiter参数用于分隔值的字符，原始文件使用的‘,’分隔
# 原始文件每一行读取为1行，读取结果就是一个二维数组
us_data = np.loadtxt(us_data_path, delimiter=',', dtype=int)
uk_data = np.loadtxt(uk_data_path, delimiter=',', dtype=int)

# 查看打开的结果
# print(us_data.shape)
# print(us_data)
# print(np.count_nonzero(us_data != us_data_path)) # 有一个缺失值

# 添加一列国家信息，创建一个只有一列的新数组，然后拼接即可
# 我们采用数字0代表US，1代表UK，行数就是us_data的行数,一列
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int) # 传入shape参数
ones_data = np.ones((uk_data.shape[0], 1)).astype(int) # 传入shape参数

# 进行数据拼接，水平拼接,加上一列
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))

# 拼接US和UK的数据，竖直拼接
final_data = np.vstack((us_data, uk_data))
print(final_data)

