# -*- coding: cp936 -*-
# 详细见P329
# 制作世界地图，在地图上显示数字数据
# 显示北美各国家的人口数据

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Population of Countries in North America'
# 添加数据，第一个参数为标签说明，此时第二个参数是字典，国别码和对应的人口数据
wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})

# 输出矢量图文件，浏览器打开，鼠标放到国家上，会显示标签说明，国家名称，人口数据
wm.render_to_file('002_北美_区域突出地图_添加人口数据.svg')
