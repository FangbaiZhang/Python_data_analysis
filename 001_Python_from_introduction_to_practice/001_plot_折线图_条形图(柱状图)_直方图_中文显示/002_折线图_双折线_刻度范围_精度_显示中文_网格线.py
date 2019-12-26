# -*- coding: utf-8 -*-

# 导入包
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# 方法1：加上下面两句代码，推荐使用，只需要设置一行即可，后面不需要像方法2一样多次传参数
# 使用以下方式，给键传入值，值为中文字体的英文名称：黑体=SimHei,宋体=SimSun
# plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 方法2：先实例化一个自定义字体格式，传入的参数为电脑系统中文字体的路径
# windows系统字体都放在Fonts里面，路径可以打开CMD窗口，拖一个中文字体到CMD窗口，
# 路径就出来了，按下Enter，会打开显示当前的字体
# 注意，自定义中文字体后，下面需要显示中文的地方还需要传入fontproperties=my_font参数
my_font = font_manager.FontProperties(fname='C:\WINDOWS\Fonts\MSYH.TTC')

# 创建数据
x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建figure窗口，指定窗口大小和分辨率
plt.figure(dpi=128, figsize=(8, 6))
# 画曲线1,其中color可以简写为c，linestyle可以简写为ls,推荐全写,label是图例
plt.plot(x, y1, label='图例: sin(x)', color='red', linewidth=3.0, linestyle='-.')
# 画曲线2
plt.plot(x, y2, label='图例: cos(x)', color='blue', linewidth=5.0, linestyle='--')


# 设置坐标轴范围,起点和端点
# plt.xlim((-5, 5))
# plt.ylim((-2, 2))

# 设置图表名称和坐标轴名称
plt.title("双折线图", fontsize=24, fontproperties=my_font)
plt.xlabel('横坐标标题', fontsize=14, fontproperties=my_font)
plt.ylabel('纵坐标标题', fontsize=14, fontproperties=my_font)

# 设置坐标轴刻度，刻度间隔
my_x_ticks = np.arange(-5, 5.5, 1)
my_y_ticks = np.arange(-2, 2.0, 0.5)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)

# 显示网格线，显示图例，注意该处显示中文的参数是prop，alpha透明度
plt.grid(axis='both', color='grey', linestyle='-.', alpha=0.2)
plt.legend(prop=my_font, loc='upper left')

# 显示出所有设置
plt.show()
