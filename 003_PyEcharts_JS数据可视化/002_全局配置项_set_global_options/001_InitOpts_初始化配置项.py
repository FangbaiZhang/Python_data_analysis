# -*- coding: utf-8 -*-

# InitOpts：初始化配置
# 类路径: class pyecharts.options.InitOpts

# 初始化配置主要用于用途：
# 画布宽度高度，背景色，图表主题，图表ID
# 使用方法：Bar(init_opts=opts.InitOpts(width='900px', height='500px', bg_color='white'))

# 参考网址：https://pyecharts.org/#/zh-cn/global_options?id=initopts%ef%bc%9a%e5%88%9d%e5%a7%8b%e5%8c%96%e9%85%8d%e7%bd%ae%e9%a1%b9

class InitOpts(
    # 图表画布宽度
    width: str = "900px",

    # 图表画布高度
    height: str = "500px",

    # 图表 ID
    chart_id: Optional[str] = None,

    # 渲染风格，可选 "canvas", "svg"
    renderer: str = RenderType.CANVAS,

    # 网页标题
    page_title: str = "Awesome-pyecharts",

    # 图表主题
    theme: str = "white",

    # 图表背景颜色
    bg_color: Optional[str] = None,

    # 远程 js host
    js_host: str = "",
)

