# -*- coding:utf-8 -*-
# 绘制折线图，坐标是字符串数据

import matplotlib.pyplot as plt
import random
import matplotlib

# 设置支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签，SimHei是黑体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 生成数据
x = range(0, 120)
print(x)
# 生成120个20到35之间的随机整数
y = [random.randint(20, 35) for i in range(120)]

# 画图步骤
# 第一步:设置图片大小长宽，设置分辨率dpi
plt.figure(figsize=(10, 8), dpi=128)

# 第二步:传入数据，和线条的基本参数
# 默认第一个参数是x坐标，第二个y坐标，指定线条宽度
plt.plot(x, y, color='red', linewidth=5, linestyle='-.')

# 第三步:调整美化图片
# 设置图片，X轴，Y轴标题
plt.title("10点到12点气温变化", fontsize=24)
plt.xlabel("时间", fontsize=14)
plt.ylabel("温度(C)", fontsize=14)

# 设置刻度标记字体的大小
plt.tick_params(axis='both', labelsize=14)
# 设置坐标轴范围
plt.ylim((10, 40))

# 取2小时的数据，+=拼接两个列表
_xtick_labels = ['10点{}分'.format(i) for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]
print(_xtick_labels[:10])
print(_xtick_labels[110:])

# xticks可以传入两个参数
# 数字和字符串一一对应，数据的长度保持一样，设置x坐标顺时针旋转45
# 列表按给定步长取出里面的部分元素，步长数据要一致
new_x_1 = list(x)[::10]
new_x_2 = _xtick_labels[::10]
plt.xticks(new_x_1, new_x_2, rotation = 45)

# 第四步：绘制显示图形
plt.show()
