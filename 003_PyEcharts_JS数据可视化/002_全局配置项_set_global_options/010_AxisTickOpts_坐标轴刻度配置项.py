class AxisTickOpts(
    # 是否显示坐标轴刻度。
    is_show: bool = True,

    # 类目轴中在 boundaryGap 为 true 的时候有效，可以保证刻度线和标签对齐。
    is_align_with_label: bool = False,

    # 坐标轴刻度是否朝内，默认朝外。
    is_inside: bool = False,

    # 坐标轴刻度的长度。
    length: Optional[Numeric] = None,

    # 坐标轴线风格配置项，参考 `series_optionsLineStyleOpts`
    linestyle_opts: Union[LineStyleOpts, dict, None] = None,
)