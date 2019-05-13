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
        # 堆叠显示，加入堆叠系列名称，同一个系统堆叠在同一个柱子上,不堆叠的不传参数
        .add_yaxis('商家A', Faker.values(), stack='stack1')
        # 隐藏某系列数据False,隐藏后图例是灰色，点击就可以显示出来,默认参数是True显示
        .add_yaxis('商家B', Faker.values(), stack='stack1', is_selected=True)
        .add_yaxis('商家C', Faker.values())
        # 柱状图的每个商品的数量是显示在柱子顶部,翻转后数据要显示在右侧
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color='black', position='top'))
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