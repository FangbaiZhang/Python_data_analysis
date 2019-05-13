# -*- coding:utf-8 -*-

import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar

# 定义一个日历图方法
def calendar_base():
    # 创建数据
    begin = datetime.date(2017, 1, 1) # 输出结果2017-01-01
    end = datetime.date(2017, 12, 31) # 输出结果2017-12-31
    # 生成日期和对应的数据，日期是字符串，数据是int
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range((end - begin).days + 1)
    ]

    # 绘制日历图
    calendar = (
        # 日历图实例
        Calendar()
        # 添加数据
        .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
        # 设置全局配置
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                min_=500,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return calendar

if __name__ == '__main__':
    # 输出文件
    calendar_base().render()




begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]
print(begin)
print(end)
print(data[:10])