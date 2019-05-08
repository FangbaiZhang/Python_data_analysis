# -*- coding:utf-8 -*-
# 绘制折线图，坐标是字符串数据

import matplotlib.pyplot as plt
import random

# 生成数据
x = range(0, 120)
print(x)
# 生成120个20到35之间的随机整数
y = [random.randint(20, 35) for i in range(120)]

# 画图步骤
# 第一步:设置图片大小长宽，设置分辨率dpi
plt.figure(figsize=(20, 8), dpi=128)

# 第二步:传入数据，和线条的基本参数
# 默认第一个参数是x坐标，第二个y坐标，指定线条宽度
plt.plot(x, y, linewidth=5, linestyle='-.')

# 第三步:调整美化图片
# 设置图片，X轴，Y轴标题
plt.title("Random Numbers", fontsize=24)
plt.xlabel("X-Value", fontsize=14)
plt.ylabel("Y-Value", fontsize=14)

# 设置刻度标记字体的大小
plt.tick_params(axis='both', labelsize=14)

# x列表按步长10取出里面的部分元素
_x = list(x)[::10]
print(_x)
# 循环取出列表中的数字加入到字符串中
_xtick_labels = ['hello,{}'.format(i) for i in _x]
print(_xtick_labels)

# xticks可以传入两个参数，长度一样，一一对应的数字和字符串
plt.xticks(_x, _xtick_labels)

# 第四步：绘制显示图形
plt.show()
