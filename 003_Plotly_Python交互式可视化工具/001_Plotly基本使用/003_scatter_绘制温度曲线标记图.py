# -*- coding: utf-8 -*-

import plotly.offline as of
import numpy as np
import plotly.graph_objs as go

# 离线模式说明:
# 设置离线模式画图,图形绘制后会自动生成并打开一个HTML文件
# 然后可以下载图片，但是图片分辨率有限制
# 可以采用截图或者将网页另存为文件的方式获取大图
of.offline.init_notebook_mode(connected=True)

# 3月和10月每天的气温
y_3 = [8,10,16,11,12,11,12,16,10,12,14,16,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,15,13,17,10,11,13,12,13,6]

# 设置两个X的坐标，10月份的右移50个点
x_3 = list(range(1, 32))
x_10 = list(range(51, 82))

# 传入数据来源，选择图形模式
trace1 = go.Scatter(
    x = x_3,
    y = y_3,
    mode = 'lines+markers',
    name = '3月气温',
)

trace2 = go.Scatter(
    x = x_10,
    y = y_10,
    mode = 'lines+markers',
    name = '10月气温',
)

# 设置图例标题刻度等
layout= go.Layout(
    title= '成都3月和10月气温变化曲线',
    hovermode= 'closest',
    xaxis= dict(
        title= '日期',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= '气温(C)',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= True
)

# 传入绘图数据
data = [trace1, trace2]

# 传入绘图数据和自定义图层数据
fig = go.Figure(data=data, layout=layout)

# 绘图
of.plot(fig)