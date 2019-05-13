# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#创建自变量数组
x= np.linspace(0,2*np.pi,500)
#创建函数值数组
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x*x)

#创建图形
plt.figure(figsize=(10, 8), dpi=128)


'''
多图形绘制需要设置图形所在位置：
subplot(numRows, numCols, plotNum)
前两个参数自动将图形分隔为几行几列，
第三个参数为从左上角开始，从左到右，从上到下图形所在的位置
如果有一行只有一列，那么其它行不同列也当做一个整体，就是一列
比如下面：subplot(2,2,1),分成2行2列的第1个元素
subplot(2,2,2),分成2行2列的第2个元素
subplot(2,1,2),分成2行1列的第2个元素,第一行所有列当做一个整体
'''

# 设置绘制图形的位置
#第一行第一列图形
ax1 = plt.subplot(2,2,1)
#第一行第二列图形
ax2 = plt.subplot(2,2,2)
#第二行的一个图形
ax3 = plt.subplot(2,1,2)

# 绘制ax1,先传入图形位置
plt.sca(ax1)
# 绘制红色曲线
plt.plot(x, y1, label='sin(x)', color='red', linestyle='--')
# 限制y坐标轴范围
plt.ylim(-1.2,1.2)
# 显示图例
plt.legend(loc='upper center')


# 绘制ax2
plt.sca(ax2)
# 绘制蓝色曲线，线条颜色和风格可以使用以下缩写方式
plt.plot(x, y2, 'b--', label='cos(x)')
plt.ylim(-1.2,1.2)
# 显示图例
plt.legend(loc='upper center')

# 绘制ax3
plt.sca(ax3)
plt.plot(x, y3, 'y-.', label='sin(x*x)')
plt.ylim(-1.2,1.5)
# 显示图例
plt.legend(loc='upper center')


plt.show()

