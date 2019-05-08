# -*- coding:utf-8 -*-
# Page186

import numpy as np

# 生成一维数组，步长为2
b = np.arange(0, 20, 2)
print(b)
print("*" * 50)

# 一维数组操作和列表类似
# 切片
print(b[1])
print("*" * 50)

print(b[0:4])
# 可以for循环取出元素
for i in b[0:4]:
    print(i)
print("*" * 50)

# 也可以使用负值操作,间隔也是负数
print(b[-1:-6:-2])
print("*" * 50)

# 分片操作，传入三个数字，第一个是起始值，第二个是终点值，第三个是步长（间隔）赋值
# 从第2个元素开始到第8个元素，以2为间隔的值，赋值为1
b[1:8:2] = 1
print(b)
