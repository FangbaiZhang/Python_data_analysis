# -*- coding: cp936 -*-
# 详细见P329
# 北美中美南美_区域突出地图
# 我们给定的区域进行突出显示，点击图形中的标签可以隐藏标签对应的地图，放在地图上会自动显示国家的名称

import pygal_maps_world.maps

# 创建一个地图绘制实例
# pygal_maps_world.maps.World()类专门用于绘制地图
# 可以输出各种格式的图形
wm = pygal_maps_world.maps.World()

# 设置图形标题
wm.title = 'North, Central, and South America'
# add方法接收一个标签和列表，第一个是参数是说明标签，第二个列表接收我们要突出的国别码
# 添加在同一个add中的归为一类，有相同的标签和颜色
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

# 输出矢量图，浏览器打开，点击图形中的标签可以隐藏标签对应的地图，放在地图上会自动显示国家的名称
wm.render_to_file('001_北美中美南美_区域突出地图.svg')
