# -*- coding:utf-8 -*-

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter

def line_base():
    c = (
        Scatter()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .set_global_opts(
            # 显示标题
            title_opts=opts.TitleOpts(title="Scatter-基本示例"),
            # 显示网格线
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            # 显示可视化图形条
            visualmap_opts=opts.VisualMapOpts(max_=150),
        )
    )

    # 绘制图片
    pic = c.render()
    return pic

if __name__ == '__main__':
    line_base()