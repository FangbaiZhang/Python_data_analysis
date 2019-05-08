# -*- coding: utf-8 -*-

# 导入包
import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 3月和10月每天的气温
y_3 = [8,10,16,11,12,11,12,16,10,12,14,16,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,15,13,17,10,11,13,12,13,6]

# 设置两个X的坐标，10月份的右移50个点
x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置图形的大小
plt.figure(figsize=(10, 6), dpi=128)

# 画曲线1,label是图例
plt.plot(x_3, y_3, 'b-.', label='3月气温' )
# 画曲线2
plt.plot(x_10, y_10, 'r--', label='10月气温')

# 调整X轴的刻度，拼接日期，显示日期
# 传入绘图参数时候，按步长取出一部分日期，日期太多会显示不下，
_x = list(x_3) + list(x_10) # 共62个数据
_xtick_labels = ['3月{}日'.format(i) for i in x_3]
_xtick_labels += ['10月{}日'.format(i-50) for i in x_10]
print(_xtick_labels)
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45)

# 设置标题
plt.xlabel('日期', fontsize=14)
plt.ylabel('温度(C)', fontsize=14)
plt.title('3月和10月气温变化', fontsize=24)

# 显示图例
plt.legend(loc='upper right')

# 显示图形
plt.show()
