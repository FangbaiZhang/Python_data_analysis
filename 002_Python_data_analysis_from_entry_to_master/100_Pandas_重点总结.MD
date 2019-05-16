# Series一维索引数组

- 只有两列，第一列是index索引，第二列是values
- 可以使用series_name.index和series_name.values获取索引和值
- 使用Numpy数组的属性ndim和shape查看维度和形状
- Series取值的方式和列表类似，以下两种方式都可以
    - 以下是Series数组b
    A    0
    B    1
    C    2
    D    3
    E    4
    F    5
    - 索引的位置，数字：b[0] = 0
    - 索引的名称，字符串：b[‘A’] = 0
    - 取连续的行：b[0:2]
    - 按步长取多行：b[0:5:2]
    - 取多行，指定行数，用两个中括号：
        - b[[0, 3, 6]]
        - b[['A', 'B', 'C']]
        
# DataFrame二维索引数组

## 竖向第一列，是index,行的索引, axis=0
## 横向第一行，是columns,列的索引, axis=1

## DataFrame二维索引数组df
   1  2   3   4
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11

- 常用属性：df.index df.columns df.shape df.size
- 常用方法：
    - 获取前两行内容：df.head(2)
    - 获取末尾两行内容: df.tail(2)
    - 查看概述信息：df.info() df.describe()
    - DataFrame重新排序，指定排序规则
    - 按Count_AnimalName这一列排序，ascending默认升序
    df.sort_values(by='Count_AnimalName', ascending=False)

- 切片操作
- 取行，取列注意事项：

    - 方括号中直接写数字，表示取行，对行进行操作
    - 方括号中写字符串，表示取列，对列进行操作
    - 数据提取的最多就是: df['列标签名称']取某一列
    
    - 取一列的某几行：df['Row_Labels'][8:10]
    - 取几行的某一列：df[8:10]['Row_Labels']

- loc标签索引:
    - 注意采用loc和切片方式只取出一行的的结果类型不一样
    - 切片取出来的还是二维索引数组，loc取出来是Series一维数组了
    - 切片取出的结果DataFrame:
       W  X  Y  Z
    a  0  1  2  3
    <class 'pandas.core.frame.DataFrame'>
    - loc索引标签取出的结果是Series：
    W    0
    X    1
    Y    2
    Z    3
    Name: a, dtype: int32
    <class 'pandas.core.series.Series'>
    
- loc多行多列，结果都是DataFrame
    - 取连续多行，使用冒号和一个中括号
    - loc['a':'c']
    - 不连续多行，逗号和两个中括号
    - loc[['a', 'c']]
    
- loc取多个值
    - loc[['a','c'], ['W', 'Z']]
    
- loc只取列
    - 行的位置使用：,代表所有的行
    - loc[:, 'Y':'Z']
    
- iloc标签位置索引
    - 使用方法和loc一样，不过是使用标签名称所在行列的位置
    - loc['a':'c', ['W', 'Z']]
    - iloc[0:3, [0, 3]]

    
    



