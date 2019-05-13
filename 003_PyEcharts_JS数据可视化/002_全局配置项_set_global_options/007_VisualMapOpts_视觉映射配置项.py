class VisualMapOpts(
    # 映射过渡类型，可选，"color", "size"
    type_: str = "color",

    # 指定 visualMapPiecewise 组件的最小值。
    min_: Union[int, float] = 0,

    # 指定 visualMapPiecewise 组件的最大值。
    max_: Union[int, float] = 100,

    # 两端的文本，如['High', 'Low']。
    range_text: Union[list, tuple] = None,

    # visualMap 组件过渡颜色
    range_color: Union[List[str]] = None,

    # visualMap 组件过渡 symbol 大小
    range_size: Union[List[int]] = None,

    # 如何放置 visualMap 组件，水平（'horizontal'）或者竖直（'vertical'）。
    orient: str = "vertical",

    # visualMap 组件离容器左侧的距离。
    # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'left', 'center', 'right'。
    # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
    pos_left: Optional[str] = None,

    # visualMap 组件离容器右侧的距离。
    # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_right: Optional[str] = None,

    # visualMap 组件离容器上侧的距离。
    # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
    # 也可以是 'top', 'middle', 'bottom'。
    # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
    pos_top: Optional[str] = None,

    # visualMap 组件离容器下侧的距离。
    # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
    pos_bottom: Optional[str] = None,

    # 对于连续型数据，自动平均切分成几段。默认为5段。连续数据的范围需要 max 和 min 来指定
    split_number: int = 5,

    # 组件映射维度
    dimension: Optional[Numeric] = None,

    # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。
    is_calculable: bool = True,

    # 是否为分段型
    is_piecewise: bool = False,

    # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
    # pieces: [
    #   {"min": 1500}, // 不指定 max，表示 max 为无限大（Infinity）。
    #   {"min": 900, "max": 1500},
    #   {"min": 310, "max": 1000},
    #   {"min": 200, "max": 300},
    #   {"min": 10, "max": 200, "label": '10 到 200（自定义label）'},
    #   {"value": 123, "label": '123（自定义特殊颜色）', "color": 'grey'}, //表示 value 等于 123 的情况
    #   {"max": 5}     // 不指定 min，表示 min 为无限大（-Infinity）。
    # ]
    pieces: Optional[Sequence] = None,

    # 定义 在选中范围外 的视觉元素。（用户可以和 visualMap 组件交互，用鼠标或触摸选择范围）
    #  可选的视觉元素有：
    #  symbol: 图元的图形类别。
    #  symbolSize: 图元的大小。
    #  color: 图元的颜色。
    #  colorAlpha: 图元的颜色的透明度。
    #  opacity: 图元以及其附属物（如文字标签）的透明度。
    #  colorLightness: 颜色的明暗度，参见 HSL。
    #  colorSaturation: 颜色的饱和度，参见 HSL。
    #  colorHue: 颜色的色调，参见 HSL。
    out_of_range: Optional[Sequence] = None,

    # 文字样式配置项，参考 `series_options.TextStyleOpts`
    textstyle_opts: Union[TextStyleOpts, dict, None] = None,
)