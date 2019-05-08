# -*- coding: cp936 -*-
# ��ϸ��P297
# �������,���ӻ�
# ����ɢ��ͼ

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# ֻҪ�����ڻ״̬���Ͳ��ϵ�ģ���������
while True:
    # ����һ��RandomWalk��ʵ��
    rw = RandomWalk(10000)
    rw.fill_walk()

    # ���û�ͼ���ڵĳߴ�
    plt.figure(figsize=(10, 6))

    # ����ɢ��ͼ��������ɫӳ�䣬��Եɫ��͸���ȣ��ߴ�
    plt.scatter(rw.x_values, rw.y_values, c=rw.x_values,
                cmap=plt.cm.plasma, edgecolor='none', alpha=0.3, s=5)

    # ͻ�������յ�
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolor='none', s=100)

    # ��������̶�
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # ���һ��break�������
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running == 'N':
        break




