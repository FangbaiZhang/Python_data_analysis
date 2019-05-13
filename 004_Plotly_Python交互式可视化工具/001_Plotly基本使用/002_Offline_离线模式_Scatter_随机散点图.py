# -*- coding: utf-8 -*-

import plotly.offline as of
import numpy as np
import plotly.graph_objs as go

# 离线模式说明:
# 设置离线模式画图,图形绘制后会自动生成并打开一个HTML文件
# 然后可以下载图片，但是图片分辨率有限制
# 可以采用截图或者将网页另存为文件的方式获取大图
of.offline.init_notebook_mode(connected=True)


# 生成1000个符合标准正态分布的数
random_x = np.random.randn(1000)
random_y = np.random.randn(1000)

# 传入数据来源，选择图形模式
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

# 传入绘图数据
data = [trace]

# 绘图
of.plot(data)