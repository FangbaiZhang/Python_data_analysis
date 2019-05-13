from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Pie

def pie_radius() -> Pie:
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["30%", "75%"], # 内环和外环占圆环直径的比例
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-Radius"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="15%", pos_left="2%" #图例离顶部和左侧的距离
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")) # 每部分文字的说明格式
    )
    return c

if __name__ == '__main__':
    # 输出文件
    pie_radius().render()