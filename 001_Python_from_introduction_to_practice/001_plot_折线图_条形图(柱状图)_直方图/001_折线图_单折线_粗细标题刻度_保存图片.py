# -*- coding:utf-8 -*-
# 绘制简单的折线图
# 当给plot提供数据时，默认数据第一个值对应的x坐标为0，所以画出的图形不指定x坐标，起始对应的x为0
# 因此画图时，同时给定x和y坐标的数据

import matplotlib.pyplot as plt

# 指定x坐标
input_values = [1, 2, 3, 4 , 5]
# 指定y坐标
squares = [1, 4, 9 , 16, 25]

# 画图步骤
# 第一步:设置图片大小长宽，设置分辨率dpi
plt.figure(figsize=(10, 8), dpi=128)


# 第二步:传入数据，和线条的基本参数
# 默认第一个参数是x坐标，第二个y坐标，指定线条宽度
plt.plot(input_values, squares, linewidth=5, linestyle='-.')


# 第三步:自定义美化
# 设置图表和坐标轴的标题和字体大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)


# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 设置x,y坐标轴的取值范围
plt.axis([0, 6, 0, 26])
# 如果单独设置x和y，使用xlim([0, 6])和ylim([0, 26])
# 也可以使用以下方式指定X轴的范围和刻度间隔步长
# plt.xticks(range(0, 10, 2))



# 第四步：绘制显示或者保存图片
# 绘制显示图形
plt.show()

# 保存图形为图片,第一个参数保存路径，第二个参数裁掉多余的空白部分
# 保存格式可以选择svg格式，矢量图放大也不会模糊
plt.savefig('001_折线图_单折线_粗细标题刻度_保存图片.jpg', bbox_inches='tight')


