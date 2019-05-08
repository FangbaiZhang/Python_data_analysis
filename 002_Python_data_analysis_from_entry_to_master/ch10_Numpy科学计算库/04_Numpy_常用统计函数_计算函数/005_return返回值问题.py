# -*- coding:utf-8 -*-

# 004中用到了return返回值
# return放置位置不同返回值不同

# 下面两种方法：
# 第一种只执行了一次循环就return了，for循环就结束了，循环一次，值还没有修改，所以值跟a一样，
# 第二种是循环完了才return的，所以值就变了

# return就退出函数了，没有后续函数内部的操作



def funa(b):
    for i in range(len(b)):
        if i > 2:
            b[i] = 0
        return b


def func(b):
    for i in range(len(b)):
        if i > 2:
            b[i] = 0
    return b

if __name__ == '__main__':
    a = list(range(5))
    print(a)
    print(funa(a))
    print(func(a))



