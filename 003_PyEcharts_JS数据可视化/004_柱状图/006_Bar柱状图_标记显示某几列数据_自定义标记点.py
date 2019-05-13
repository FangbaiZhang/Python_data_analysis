# -*- coding:utf-8 -*-

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

def bar_base():
    x, y = Faker.choose(), Faker.values()
    # 采用链式写法,先传入所有的数据和配置
    c = (
        Bar()
        # 传入X轴数据,选择七个品类中的一种中的七样东西
        .add_xaxis(x)
        .add_yaxis(
            "商家A",
            y,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
            ),
        )
        .add_yaxis(
            "商家B",
            y,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="自定义标记点", coord=[x[4], y[4]], value=y[4])]
            ),
        )          

        #不显示数据标记,只显示上面自定义的标记点
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

        # 设置全局配置项
        .set_global_opts(
            # 显示主副标题
            title_opts=opts.TitleOpts(title='主标题:商家', subtitle='副标题:销售记录'),
            # 显示工具栏,工具栏用于刷新图片，下载图片，查看图片数据等
            toolbox_opts=opts.ToolboxOpts(),
            # 隐藏图例False，默认显示图例True,没有该设置，默认所有图例都显示
            legend_opts=opts.LegendOpts(is_show=True),
            # 设置Y轴坐标刻度，由于堆叠以后数据超过单独的最大数据150,需要将刻度调整
            yaxis_opts=opts.AxisOpts(min_=0, max_=300)
        )
    )

    # 绘制图片
    pic = c.render()
    return pic

if __name__ == '__main__':
    bar_base()