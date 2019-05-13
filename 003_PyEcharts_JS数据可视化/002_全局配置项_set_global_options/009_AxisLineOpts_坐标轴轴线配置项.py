class AxisLineOpts(
    # 是否显示坐标轴轴线。
    is_show: bool = True,

    # X 轴或者 Y 轴的轴线是否在另一个轴的 0 刻度上，只有在另一个轴为数值轴且包含 0 刻度时有效。
    is_on_zero: bool = True,

    # 当有双轴时，可以用这个属性手动指定，在哪个轴的 0 刻度上。
    on_zero_axis_index: int = 0,

    # 轴线两边的箭头。可以是字符串，表示两端使用同样的箭头；或者长度为 2 的字符串数组，分别表示两端的箭头。
    # 默认不显示箭头，即 'none'。
    # 两端都显示箭头可以设置为 'arrow'。
    # 只在末端显示箭头可以设置为 ['none', 'arrow']。
    symbol: Optional[str] = None,

    # 坐标轴线风格配置项，参考 `series_optionsLineStyleOpts`
    linestyle_opts: Union[LineStyleOpts, dict, None] = None,
)
