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
        .add_yaxis('商家B', Faker.values())
        .add_yaxis('商家C', Faker.values())
        # Y系列数据显示配置，柱状图的每个商品的数量是默认显示在柱子顶部,隐藏is_show=False
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='top'))
        # 设置全局配置项,显示主副标题
        .set_global_opts(title_opts=opts.TitleOpts(title='主标题:商家', subtitle='副标题:销售记录'))
    )

    # 绘制图片
    pic = c.render()
    return pic

if __name__ == '__main__':
    bar_base()