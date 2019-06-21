# -*- coding:utf-8 -*-
# Page185
# a数组是整数型，b数组是浮点型，a和b数组相加，并赋值给a，则会引发异常
# 但是 b += a则会正常计算出结果
# Numpy中对不同类型数组计算，默认有个转换规则，精度低的向精度高的数据类型转换
# b是浮点型，a是整数型，b的精度更高
import numpy as np

a = np.ones((3, 3), dtype='int32')
b = np.ones((3, 3), dtype='float64')

b += a

print(b)

# 如下方式精度高到精度低就会报错
a +=b
print(a)