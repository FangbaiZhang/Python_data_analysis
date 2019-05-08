# -*- coding:utf-8 -*-
import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
print("*" * 50)

# 求极值，最大值和最小值之差
print(np.ptp(a, axis=0))
print(np.ptp(a, axis=1))
print("*" * 50)

# 求标准差，标准差是数据平均值分散程度的一种度量
# 标准差较大，代表大部分数据与其平均值之间的差异较大
# 标准差较小，代表大部分数据与其平均值之间的差异较小
# 因此，标准差越大，代表数据波动大，不稳定，标准差小，波动小，数据稳定

# 每列的标准差,列的标准差大于行的
print(a.std(axis=0))
# 每行的标准差,不同行的标准差相同，因为都是连续的数字
print(a.std(axis=1))

