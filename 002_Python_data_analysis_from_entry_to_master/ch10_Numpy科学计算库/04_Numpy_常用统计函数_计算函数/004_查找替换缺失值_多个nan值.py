# -*- coding:utf-8 -*-
import numpy as np

# 创建一个浮点类型的数组
a = np.arange(12, dtype=float).reshape(3, 4)
print(a)
print("*" * 50)

# 将其中第2行第三列开始都改成nan
a[1, 2:] = np.nan
print(a)
print("*" * 50)

# 我们遍历进行遍历，有4列我们遍历4次
print(a.shape[1]) # 就是列数
print("*" * 50)

# 找出所有的nan，并将nan赋值为均值
def fill_ndarray(a):
    for i in range(a.shape[1]):
        # 当前的一列
        temp_col = a[:, i]
        # 由于任何nan都不相等,自己不等于自己，nan对应布尔值为True即1,统计出不为0的数即所有的nan
        nan_num = np.count_nonzero(temp_col != temp_col)
        # 如果统计的nan数不等于0,把这一列提取出来
        if nan_num != 0:
            # 取出当前列中不为nan的数组，temp_col == temp_col找出所有相等的值，就是不是nan的值
            temp_not_nan_col = temp_col[temp_col == temp_col]
            # 求出当前列不为nan所有值的平均值，然后赋值给当前列为nan的位置
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
        # nan修改赋值后，返回新的数组
    return a

if __name__ == '__main__':
    t = np.arange(12, dtype=float).reshape(3, 4)
    t[1, 2:] = np.nan
    print("修改前:")
    print(t)
    print("修改后:")
    b = fill_ndarray(t)
    print(b)


# 上面这种方法比较麻烦，Pandas里面有修改缺失值的简单方法







