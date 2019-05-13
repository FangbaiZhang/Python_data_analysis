# -*- coding:utf-8 -*-

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Line

def line_base():
    x, y1, y2 = Faker.choose(), Faker.values(), Faker.values()
    c = (
        Line()
        # 传入X轴数据,选择七个品类中的一种中的七样东西
        .add_xaxis(x)
        # 传入Y轴数据，第一个参数是系列的名称，第二个参数是数据(随机选择20-150之间的整数)
        .add_yaxis(
            '商家A',
            y1,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name='最大值', type_="max")]),
        )
        # 隐藏某系列数据False,隐藏后图例是灰色，点击就可以显示出来,默认参数是True显示
        .add_yaxis(
            '商家B',
            y2,
            is_selected=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(
                    name="自定义标记点", coord=[x[2], y2[2]], value=y2[2])
                ]
            ),
        )

        # 设置数据配置项
        # 每个商品的数量是显示在点的上部，改变数据的颜色
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color='red', position='top'))


        # 设置全局配置项
        .set_global_opts(
        # 显示主副标题
        title_opts=opts.TitleOpts(title='主标题:商家', subtitle='副标题:销售记录'),
        # 显示工具栏,工具栏用于刷新图片，下载图片，查看图片数据等
        toolbox_opts=opts.ToolboxOpts(),
        # 隐藏图例False，默认显示图例True,没有该设置，默认所有图例都显示
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置Y轴坐标刻度
        yaxis_opts=opts.AxisOpts(min_=0, max_=180)
        )
    )

    # 绘制图片
    pic = c.render()
    return pic

if __name__ == '__main__':
    line_base()