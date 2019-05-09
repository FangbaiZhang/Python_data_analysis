# Plotly可视化入门到精通(Python版)

## 简介
- Plotly：
    - 一个用于做分析和可视化的在线平台，曾被网友称为“有史以来最牛逼”可视化神器，为何有如此称号？
    - 因为它功能强大，功能强大，功能强大！重要的事情说三遍！其功能强大到不仅与多个主流绘图软件的对接，
    - 而且还可以像Excel那样实现交互式制图，而且图表种类齐全，并可以实现在线分享以及开源，等等；
    - 这种功能强大到还没有一个人能够完全掌握其全部应用，甚至国内对它的介绍使用也仅仅只是其中一部分。
    - 接下来笔者结合python的使用来介绍Plotly的使用。

- 图表类型：
    - 基本图表：20种；统计和海运方式图：12种；
    - 科学图表：21种；财务图表：2种；地图：8种；
    - 3D图表：19种；拟合工具：3种；流动图表：4种

## 1. 安装Plotly
- 要安装Plolyly的python包，请在您的终端中使用软件包管理器pip。
- 推荐清华源下载whl文件后安装，在线安装速度太慢
- 安装命令
    - $ pip install plotly 
    - $ sudo pip install plotly 
    - $ pip install plotly --upgrade
    
## 2. 在线绘图模式
- Plotly为托管图形提供了web服务!创建一个免费帐户开始。
- 图形保存在您的在线Plotly帐户中，您可以控制隐私。
- 公共托管是免费的，对于私人托管，请查看我们的付费计划。
- 2019年开始公共托管只能托管25个图形，开心的使用需要付费
- 学生用户，一年99美元，初学者推荐使用离线模式，绘图功能一样

- 在线模式绘图前要进行以下设置，导入包，然后设置你的用户名和API-KEY
- API-KEY进入个人账号-settings-API-KEY,生成即可
    - import plotly 
    - plotly.tools.set_credentials_file(username='username', api_key='xxxxxxxxx')

- 注意：默认你的绘图上传到网站是公开的，如果要私有，进行以下设置
    - plotly.tools.set_config_file(world_readable=False, sharing='private')

- 在线模式绘图案例：
    - 001_Online_在线模式_Scatter_随机散点图
    
## 3. 离线绘图模式
- 离线绘图模式说明
    - 设置离线模式画图,图形绘制后会自动生成并打开一个HTML文件
    - 然后可以下载图片，但是图片分辨率有限制
    - 可以采用截图或者将网页另存为文件的方式获取大图

- 离线绘图进行以下设置即可
    - import plotly.offline as of
    - of.offline.init_notebook_mode(connected=True)
    
- 离线模式绘图案例
    - 002_Offline_离线模式_Scatter_随机散点图