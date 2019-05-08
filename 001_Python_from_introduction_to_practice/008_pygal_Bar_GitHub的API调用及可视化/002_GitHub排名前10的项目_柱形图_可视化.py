# -*- coding: cp936 -*-
# 详细见P345
# 执行API调用，找出GitHub上评分最高的项目

import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# 打印一个状态码，看请求网址是否成功
print("Status code:", r.status_code)

# 获取到的网址信息，其实就是一个类似字典的信息，将API响应存储在一个字典中
response_dict = r.json()
# 处理结果,打印出获取的到字典中的键，和网页对比，发现没有问题
print(response_dict.keys())
print("Total repositories:", response_dict['total_count']) # 打印总条目

# 探索有关仓库的信息,items对应的是一个列表，列表中包含很多字典
repo_dicts = response_dict['items']

# 可视化仓库的信息,将仓库名称和对应评分提取到列表中
names, stars = [], []
for repo_dict in repo_dicts[0:10]:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 绘制矢量图

# 设置图形风格
my_style = LS('#993366', base_style=LCS)

# 创建一个Config实例，用于自定义图形的外观
my_config = pygal.Config()
# X轴旋转30度和显示图例
my_config.x_label_rotation = 30
my_config.show_legend = True
# 设置标题和刻度大小
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# 较长的字符缩短为14个字符
my_config.truncate_label = 15
# 隐藏图中水平线
my_config.show_y_guides = False
# 定义图表宽度
my_config.width = 1000


# 绘制柱形图，第一个实参就是自定义配置
chart = pygal.Bar(my_config, style=my_style)
# 设置图表标题
chart.title = 'Most-Starred Python Projects on GitHub'
# 设置X轴数据
chart.x_labels = names
# 添加Y轴数据
chart.add('Stars', stars)
# 输出图片
chart.render_to_file('002_GitHub排名前10的项目_柱形图_可视化.svg')


 

