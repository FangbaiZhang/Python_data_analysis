

class ToolBoxFeatureOpts(
    # 保存为图片
    save_as_image: Optional[dict] = None,

    # 配置项还原
    restore: Optional[dict] = None,

    # 数据视图工具，可以展现当前图表所用的数据，编辑后可以动态更新
    data_view: Optional[dict] = None,

    # 数据区域缩放。目前只支持直角坐标系的缩放
    data_zoom: Optional[dict] = None,
)