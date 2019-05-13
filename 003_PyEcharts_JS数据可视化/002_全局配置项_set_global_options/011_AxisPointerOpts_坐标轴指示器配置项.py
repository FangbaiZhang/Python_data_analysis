class AxisPointerOpts(
    # 默认显示坐标轴指示器
    is_show: bool = True,

    # 指示器类型。
    # 可选参数如下，默认为 'line'
    # 'line' 直线指示器
    # 'shadow' 阴影指示器
    # 'none' 无指示器
    type_: str = "line",

    # 坐标轴指示器的文本标签，坐标轴标签配置项，参考 `series_options.LabelOpts`
    label: Union[LabelOpts, dict, None] = None,

    # 坐标轴线风格配置项，参考 `series_optionsLineStyleOpts`
    linestyle_opts: Union[LineStyleOpts, dict, None] = None,
)