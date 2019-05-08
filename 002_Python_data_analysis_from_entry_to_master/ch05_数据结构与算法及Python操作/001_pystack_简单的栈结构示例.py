# -*- coding:utf-8 -*-
# Page85
# 一个简单的栈结构示例
# 栈可以看做同一个位置进行插入和删除的表，这个位置称作栈顶
# 栈可以看做一个容器，先进栈的数据保存在容器底部，后进的保存在顶部，特性就是后进先出LIFO last in first out
# 主要有两个方法:进栈PUSH方法，出栈POP方法

import time

# 创建一个栈类
class PyStack():

    def __init__(self, size=20):
        self.stack = []                                 # 栈列表
        self.size = size                                # 栈大小
        self.top = -1                                   # 栈顶位置，最后进的一个元素位置

    def setSize(self, size):
        self.size = size                                # 设置栈大小

    def push(self, element):                            # 设置元素进栈方法
        if self.isFull():
            raise StackException('PyStackOverflow')     # 如果栈满，则引发异常
        else:
            self.stack.append(element)
            self.top = self.top + 1

    def pop(self):                                      # 设置元素出栈方法
        if self.isEmpty():
            raise StackException('PyStackUnderflow')    # 如果栈为空，则引发异常
        else:
            element = self.stack[-1]
            self.top = self.top - 1
            del self.stack[-1]
            return element

    def Top(self):                                      # 获取栈顶位置
        return self.top

    def empty(self):                                    # 清空栈
        self.stack = []
        self.top = -1

    def isEmpty(self):                                  # 是否为空栈
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):                                       # 是否为满栈
        if self.top == self.size - 1:
            return True
        else:
            return False

# 自定义一个异常类
class StackException(Exception):

    def __init__(self, data):                               # 类实例化自动执行
        self.data = data

    def __str__(self):                                      # 类打印或格式化输出时候执行
        return self.data

if __name__ == '__main__':
    # 创建一个栈实例
    stack = PyStack()

    # 元素进栈
    for i in range(10):
        stack.push(i)
    # 输出栈顶位置，因为栈顶初始值是-1，进一个元素栈顶就是0，进10个就是10-1=9
    print("元素进栈后的栈顶位置:")
    print(stack.Top())

    # 元素出栈,pop方法执行后返回值是出栈的元素,最上面的元素是9,依次出栈，后进先出
    print("元素从栈顶开始依次出栈:")
    for i in range(10):
        print(stack.pop())
    print("元素出栈后的栈顶位置")
    print(stack.Top())

    # 主动引发异常，由于容器最大20个元素，进栈21个引发异常
    # 等待上面代码全部执行完毕
    time.sleep(3)
    print("我出现了以下异常:")
    for i in range(21):
        stack.push(i)









