# -*- coding:utf-8 -*-
# Page87
# 一个简单的队列结构示例
# 队列和栈结构类似，不同的是队列的出队操作是在队首元素执行删除操作
# 特性就是先进先出FIFO first in first out
# 主要有两个方法:进队IN方法，出对OUT方法

import time

# 创建一个队列类
class PyQueue():

    def __init__(self, size=20):
        self.queue = []                                 # 队列
        self.size = size                                # 队列大小
        self.end = -1                                   # 队尾位置，最后进的一个元素位置

    def setSize(self, size):
        self.size = size                                # 设置队列大小

    def In(self, element):                              # 设置元素入队方法
        if self.end < self.size - 1:
            self.queue.append(element)
            self.end = self.end + 1
        else:
            raise QueueException('PyQueueFull')         # 如果队列满，则引发异常

    def Out(self):                                      # 设置元素出队方法
        if self.end != -1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end = self.end - 1
            return element
        else:
            raise QueueException('PyQueueEmpty')        # 如果队列为空，则引发异常

    def End(self):                                      # 获取队尾位置
        return self.end

    def empty(self):                                    # 清空队列
        self.queue = []
        self.end = -1

# 自定义一个异常类
class QueueException(Exception):

    def __init__(self, data):                               # 类实例化自动执行
        self.data = data

    def __str__(self):                                      # 类打印或格式化输出时候执行
        return self.data

if __name__ == '__main__':
    # 创建一个队列实例
    queue = PyQueue()

    # 元素入队
    for i in range(10):
        queue.In(i)
    # 输出队尾位置，因为队尾初始值是-1，进一个元素队尾就是0，进10个就是10-1=9
    print("元素入队后的队尾位置:")
    print(queue.End())

    # 元素出队,Out方法执行后返回值是出队的元素,队首的元素是1,依次出队，先进先出
    print("元素从队首开始依次出队:")
    for i in range(10):
        print(queue.Out())
    print("元素出对后的队尾位置")
    print(queue.End())

    # 主动引发异常，由于容器最大20个元素，入队21个引发异常
    # 等待上面代码全部执行完毕
    time.sleep(3)
    print("我出现了以下异常:")
    for i in range(21):
        queue.In(i)









