# -*- coding:utf-8 -*-
# Page175
# reshape方法将数组转换为指定维度，返回新的数组
# size方法输出数组的大小(里面有多少个元素），数组大小就是shape元组内元素的乘积

import numpy as np

t1 = np.arange(12)
print(t1)
print("*" * 50)

# 转换为二维数组，上面12数据转换为3行4列
t2 = t1.reshape((3, 4))
print(t2)
print("*" * 50)
# 转换为三维数组,上面12数据转换为2个块，3行， 如果最后一个参数为-1,会根据size和其它参数自动计算该参数，
t3 = t1.reshape((2, 3, -1))
print(t3)
print("*" * 50)

# t3转换一维数组
t4 = t3.reshape((12,))
print(t4)
print("*" * 50)

# 转换为一维数组快捷函数
t5 = t3.flatten()
print(t5)
print("*" * 50)


# 查看数组的size，里面有多少个元素
print(t1.size)
print(t2.size)


# dtype用于查看数组内部元素的类型
print(t1.dtype)
print(t2.dtype)
