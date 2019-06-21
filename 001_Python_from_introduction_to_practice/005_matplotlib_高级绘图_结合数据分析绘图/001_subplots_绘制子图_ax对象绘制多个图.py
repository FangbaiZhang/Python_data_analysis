# -*- coding: utf-8 -*-

# 在matplotlib中，整个图像为一个Figure对象。在Figure对象中可以包含一个或者多个Axes对象。
# 每个Axes(ax)对象都是一个拥有自己坐标系统的绘图区域

# subplot用于一个figure中绘制多个子图，多个子图是相互独立绘制的。
# subplot传入的是位置参数。参考001_plot_折线图_条形图(柱状图)_直方图中的案例

# subplots绘制子图，传入多个参数，返回子图对象
# def subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True,
             # subplot_kw=None, gridspec_kw=None, **fig_kw):
# 返回值的类型为元组，包含两个元素：第一个为一个画布，第二个是子图
# fig： matplotlib.figure.Figure 对象
# ax：子图对象（ matplotlib.axes.Axes）或者是他的数组

'''
fig,ax = plt.subplots()等价于：
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

fig, ax = plt.subplots(1,3),其中参数1和3分别代表子图的行数和列数，一共有 1x3 个子图像。
函数返回一个figure图像和子图ax的array列表,可以使用ax[x, y]指定位置。
fig, ax = plt.subplots(1,3,1),最后一个参数1代表第一个子图。
如果想要设置子图的宽度和高度可以在函数内加入figsize值
fig, ax = plt.subplots(1,3,figsize=(15,7))，这样就会有1行3个15x7大小的子图。
'''

import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成数据
# 生成30个-5到2等分元素
x = np.linspace(-5, 2, 30)
y1 = x**3 + 5*x**2 + 10
# y2是y1的导数
y2 = 3*x**2 + 10*x
# y3是y2的导数
y3 = 6*x + 10
# y4是一条曲线
y4 = x**2

# 基本绘图方法
# plt.plot(x, y1)
# plt.show()

# 高级绘图
# 对象绘图,返回一个画布，一个绘图对象，共享X轴
fig, ax = plt.subplots(2, 2, figsize=(10, 8), sharex=True)


# 注意，上面ax是plt返回的绘图对象，本来绘图设置都是plt.，后面都是使用
# 指定绘图的位置，进行绘图
ax[0, 0].plot(x, y1, 'b--')
# 添加注释,传入注释内容，注释的箭头的点坐标，注释文字的坐标位置，
# shrink设置箭头末端和文字起点的间距，箭头自己会根据箭头起点和文字起点自适应大小和倾斜角度
ax[0, 0].annotate('我是注释', xy=(-3, 30), xytext=(-1, 35), arrowprops=dict(facecolor='red', edgecolor='red', shrink=0.05))

# 每个图都可以单独设置，指定ax对象进行设置
# 绘制另外3个图

ax[0, 1].plot(x, y2, 'r--')

ax[1, 0].plot(x, y3, 'b*')
ax[1, 0].set_xlabel('x轴')

ax[1, 1].plot(x, y4, 'r*')
ax[1, 1].set_xlabel('x轴')

# 展示所有图形
plt.show()

