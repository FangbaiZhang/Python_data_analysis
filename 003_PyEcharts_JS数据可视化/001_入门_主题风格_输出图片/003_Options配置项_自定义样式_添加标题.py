# -*- coding: utf-8 -*-
# 使用options 配置项，在 pyecharts 中，一切皆 Options。
# 案例002添加标题选项
# 输出文件为图片

from pyecharts.charts import Bar
from pyecharts import options as opts

# 导入输出图片工具
# 使用snapshot-selenium 渲染图片
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

# 创建一个柱状图Bar实例
bar = (
    Bar()
    # 添加X轴数据
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    # 添加Y轴数据,系列的名称
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [8, 15, 60, 20, 25, 30])
    # 添加标题
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题: 双十一销量", subtitle="副标题:服饰类"))
)

# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，自定义名称，如 bar.render("mycharts.html")
bar.render()


# 输出保存为图片
# make_snapshot(snapshot, bar.render(), "003_Options配置项_自定义样式_保存图片.png")

