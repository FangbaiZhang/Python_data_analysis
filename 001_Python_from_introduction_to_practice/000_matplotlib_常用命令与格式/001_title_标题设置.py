# 参考博文：
# matplotlib命令与格式：标题(title)，标注(annotate)，文字说明(text)
# https://blog.csdn.net/u011318077/article/details/93173473


'''
(1)
title常用参数
fontsize设置字体大小，默认12，可选参数['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
fontweight设置字体粗细，可选参数['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
fontstyle设置字体类型，可选参数['normal' | 'italic' | 'oblique']，italic斜体，oblique倾斜
verticalalignment设置水平对齐方式 ，可选参数 ： 'center', 'top', 'bottom', 'baseline'
horizontalalignment设置垂直对齐方式，可选参数：left, right, center
rotation(旋转角度)
可选参数为: vertical, horizontal
也可以为数字
alpha透明度，参数值0至1之间
backgroundcolor标题背景颜色
bbox给标题增加外框 ，常用参数如下：
boxstyle方框外形
facecolor(简写fc)
背景颜色
edgecolor(简写ec)
边框线条颜色
edgewidth边框线条大小

(2)
title例子：
plt.title('Interesting Graph', fontsize='large'，fontweight = 'bold') 设置字体大小与格式
plt.title('Interesting Graph', color='blue')
设置字体颜色
plt.title('Interesting Graph', loc='left')
设置字体位置
plt.title('Interesting Graph', verticalalignment='bottom')
设置垂直对齐方式
plt.title('Interesting Graph', rotation=45)
设置字体旋转角度
plt.title('Interesting', bbox=dict(facecolor='g', edgecolor='blue', alpha=0.65))
标题边框
'''


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 6, 7, 9, 2]

fig, ax = plt.subplots(1, 1)
ax.plot(x, y, label='trend')
ax.set_title('title test', fontsize=12, color='r')

plt.show()