# -*- coding:utf-8 -*-

from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

# 主要主题代号:
# LIGHT-浅色系,DARK-黑色，CHALK-浅深色，ESSOS, INFOGRAPHIC,MACARONS,
# PURPLE_PASSION-背景格子色，ROMA，ROMANTIC，SHINE,VINTAGE,WALDEN,WESTEROS,WONDERLAND
# 参考网页: https://pyecharts.org/#/zh-cn/themes?id=%e4%bd%bf%e7%94%a8%e8%87%aa%e5%b7%b1%e6%9e%84%e5%bb%ba%e7%9a%84%e4%b8%bb%e9%a2%98


# 创建一个柱状图Bar实例
bar = (
    # 自定义主题，选择ThemeType直接使用系统的自带的主题风格
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
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