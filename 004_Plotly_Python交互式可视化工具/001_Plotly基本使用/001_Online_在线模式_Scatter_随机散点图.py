# -*- coding: utf-8 -*-

import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

# 在线模式说明：
# 设置在线模式绘图，需要传入用户名和密钥，密钥在个人设置的API-key里面生成
# 在线模式画图，图形生成后会自动上传到云端网站，但是免费用户最多创建25个图表
# 在线模式绘图后直接下载，分辨率高于离线模式(可以通过截图或者另存为文件获取大图)
tools.set_credentials_file(username='FelixZhang', api_key='BQwOyfMNab52Co2ZPgaw')

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
py.iplot(data, filename='basic-scatter')
