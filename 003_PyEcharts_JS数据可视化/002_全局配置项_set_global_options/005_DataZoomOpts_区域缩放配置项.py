class DataZoomOpts(
    # 是否显示 组件。如果设置为 false，不会显示，但是数据过滤的功能还存在。
    is_show: bool = True,

    # 组件类型，可选 "slider", "inside"
    type_: str = "slider",

    # 拖动时，是否实时更新系列的视图。如果设置为 false，则只在拖拽结束的时候更新。
    is_realtime: bool = True,

    # 数据窗口范围的起始百分比。范围是：0 ~ 100。表示 0% ~ 100%。
    range_start: Numeric = 20,

    # 数据窗口范围的结束百分比。范围是：0 ~ 100
    range_end: Numeric = 80,

    # 数据窗口范围的起始数值。如果设置了 start 则 startValue 失效。
    start_value: Union[int, str, None] = None,

    # 数据窗口范围的结束数值。如果设置了 end 则 endValue 失效。
    end_value: Union[int, str, None] = None,

    # 布局方式是横还是竖。不仅是布局方式，对于直角坐标系而言，也决定了，缺省情况控制横向数轴还是纵向数轴
    # 可选值为：'horizontal', 'vertical'
    orient: str = "horizontal",

    # 设置 dataZoom-inside 组件控制的 x 轴（即 xAxis，是直角坐标系中的概念，参见 grid）。
    # 不指定时，当 dataZoom-inside.orient 为 'horizontal'时，默认控制和 dataZoom 平行的第一个 xAxis
    # 如果是 number 表示控制一个轴，如果是 Array 表示控制多个轴。
    xaxis_index: Union[int, List[int], None] = None,

    # 设置 dataZoom-inside 组件控制的 y 轴（即 yAxis，是直角坐标系中的概念，参见 grid）。
    # 不指定时，当 dataZoom-inside.orient 为 'horizontal'时，默认控制和 dataZoom 平行的第一个 yAxis
    # 如果是 number 表示控制一个轴，如果是 Array 表示控制多个轴。
    yaxis_index: Union[int, List[int], None] = None,

    # 是否锁定选择区域（或叫做数据窗口）的大小。
    # 如果设置为 true 则锁定选择区域的大小，也就是说，只能平移，不能缩放。
    is_zoom_lock: bool = False,
)