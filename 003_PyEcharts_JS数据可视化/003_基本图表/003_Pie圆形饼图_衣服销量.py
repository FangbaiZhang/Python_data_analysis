from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Pie


def pie_base() -> Pie:
    c = (
        Pie()
        # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        # 添加图标上显示的标题和数据
        .add("衣服销量", [['衬衫', 63], ['毛衣', 97], ['领带', 106], ['裤子', 50], ['风衣', 41], ['高跟鞋', 108], ['袜子', 34]])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

if __name__ == '__main__':
    # 输出文件
    pie_base().render()

print([list(z) for z in zip(Faker.choose(), Faker.values())])