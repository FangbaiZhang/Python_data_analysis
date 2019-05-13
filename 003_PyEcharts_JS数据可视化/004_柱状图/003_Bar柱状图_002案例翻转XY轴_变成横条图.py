# -*- coding:utf-8 -*-

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

def bar_base():
    # 采用链式写法,先传入所有的数据和配置
    c = (
        Bar()
        # 传入X轴数据,选择七个品类中的一种中的七样东西
        .add_xaxis(Faker.choose())
        # 传入Y轴数据，第一个参数是系列的名称，第二个参数是数据(随机选择20-150之间的整数)
        .add_yaxis('商家A', Faker.values())
        # 隐藏某系列数据False,隐藏后图例是灰色，点击就可以显示出来,默认参数是True显示
        .add_yaxis('商家B', Faker.values(), is_selected=True)
        # 翻转XY轴,变成横条图,X轴竖向显示,Y轴横向显示
        .reversal_axis()
        # 柱状图的每个商品的数量是显示在柱子顶部,翻转后数据要显示在右侧
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='right'))
        # 设置全局配置项
        .set_global_opts(
            # 显示主副标题
            title_opts=opts.TitleOpts(title='主标题:商家', subtitle='副标题:销售记录'),
            # 显示工具栏,工具栏用于刷新图片，下载图片，查看图片数据等
            toolbox_opts=opts.ToolboxOpts(),
            # 隐藏图例False，默认显示图例True,没有该设置，默认所有图例都显示
            legend_opts=opts.LegendOpts(is_show=True),
        )
    )

    # 绘制图片
    pic = c.render()
    return pic

if __name__ == '__main__':
    bar_base()