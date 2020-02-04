# -*- coding: utf-8 -*-

from pyecharts.charts import Bar

# 创建一个柱状图Bar实例

bar = (
    Bar()
    .
    # 添加X轴数据
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    # 添加Y轴数据,系列的名称
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [8, 15, 60, 20, 25, 30])
)

# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，自定义名称，如 bar.render("mycharts.html")
bar.render()