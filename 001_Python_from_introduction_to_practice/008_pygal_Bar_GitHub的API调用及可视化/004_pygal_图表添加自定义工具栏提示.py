# -*- coding: cp936 -*-
# 详细见P347
# 向图表添加自定义工具提示

import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 自定义颜色风格
my_style = LS('#993366', base_style=LCS)

# 自定义图形外观，参考003案例
my_config = pygal.Config()
my_config.x_label_rotation = 30
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False

# 绘制柱形图，传入上面的参数
chart = pygal.Bar(my_config, style=my_style)
# 图形标题
chart.title = 'Python Projects'

# 添加X坐标对应的值
chart.x_labels = ['httpie', 'django', 'flask']
# 将列表中的字典传递给Y坐标，字典的第一个键对应的值为Y坐标，第二个键的值作为工具提示
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie'},
    {'value': 15028, 'label': 'Description of django'},
    {'value': 14798, 'label': 'Description of flask'},
    ]
chart.add('Star', plot_dicts)

# 输出矢量图文件
chart.render_to_file('004_pygal_图表添加自定义工具栏提示.svg')


 

