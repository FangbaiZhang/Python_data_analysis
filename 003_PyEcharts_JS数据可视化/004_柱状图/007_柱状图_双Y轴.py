# -*- coding:utf-8 -*-

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Line

def overlap_bar_line():
    bar = (
        Bar()
        .add_xaxis(Faker.months)
        .add_yaxis("蒸发量", v1)
        .add_yaxis("降水量", v2)
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Overlap-bar+line（双 Y 轴）"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} ml")
            ),
        )
    )

    line = Line().add_xaxis(Faker.months).add_yaxis("平均温度", v3, yaxis_index=1)
    bar.overlap(line)

if __name__ == '__main__':
    overlap_bar_line()