# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

from pyecharts import options as opts
from pyecharts.charts import Bar



# 使用matplotlib展示中国星巴克分布情况
# 打开星巴克文件
filepath = './starbucks_store_worldwide.csv'
df = pd.read_csv(filepath)
# 提取出属于中国的DataFrame数据
df = df[df['Country'] == 'CN']

# 提取省份数据
# 按国家分组，统计出每个国家的星巴克数量，Brand里面没有缺失数据，按这个索引统计数量
data1 = df.groupby(by='City')['Brand'].count()
# print(data1)
print('*' * 100)
# 按数量降序排列，取前十名的数据
data2 = data1.sort_values(ascending=False)[0:10]
print(data2)
print(type(data2))
print('*' * 100)

# 绘图，提取结果是一个Series一维数据，直接提取index和值
# 转换为列表
_x = list(data2.index)
_y = list(data2.values)
print(type(_x))
print(_x)
print(_y)

x = ['上海市', '北京市', '杭州市', '深圳市', '广州市', 'Hong Kong', '成都市', '苏州市', '南京市', '武汉市']
y = [542, 234, 117, 113, 106, 104, 98, 90, 73, 67]


def bar_base():
    # 采用链式写法,先传入所有的数据和配置
    c = (
        Bar()
        # 传入X轴数据
        .add_xaxis(x)
        # 传入Y轴数据，第一个参数是系列的名称，第二个参数是数据
        .add_yaxis('星巴克数量', y)
        # 设置全局配置项
        .set_global_opts(
            # 显示主副标题
            title_opts=opts.TitleOpts(title='星巴克数量', subtitle='全国前10城市'),
            # 显示工具栏,工具栏用于刷新图片，下载图片，查看图片数据等
            toolbox_opts=opts.ToolboxOpts(),
            # 隐藏图例False，默认显示图例True,没有该设置，默认所有图例都显示
            legend_opts=opts.LegendOpts(is_show=True),
            # 显示所有的横坐标，默认会自动隐藏一部分横坐标
            xaxis_opts=opts.AxisOpts(axislabel_opts={'interval': 0})
        )
    )

    # 绘制图片
    pic = c.render()
    return pic

if __name__ == '__main__':
    bar_base()
