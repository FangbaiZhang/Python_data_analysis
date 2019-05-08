# -*- coding:utf-8 -*-

# 树是一种非线性的数据结构
# 二叉树：每个节点最多只有两个儿子，分为左和右
# Page90

# 创建一个二叉树类
class BTree():

    # 初始化函数，初始化该节点只有值，还没有儿子
    def __init__(self, value):
        self.left = None #左儿子
        self.data = value #该节点的值
        self.right = None #右儿子

    # 向左子树插入节点，产生左儿子
    def insertLeft(self, value):
        self.left = BTree(value)
        return self.left

    # 向右子树插入节点，产生右儿子
    def insertRight(self, value):
        self.right = BTree(value)
        return self.right

    # 输出节点数据
    def show(self):
        print(self.data)

if __name__ == '__main__':
    # 创建根节点
    Root = BTree('Root')
    # 插入左儿子
    A = Root.insertLeft('A')
    # 插入右儿子
    B = Root.insertRight('B')
    Root.show()
    Root.left.show()
    Root.right.show()
    A.show()
    B.show()