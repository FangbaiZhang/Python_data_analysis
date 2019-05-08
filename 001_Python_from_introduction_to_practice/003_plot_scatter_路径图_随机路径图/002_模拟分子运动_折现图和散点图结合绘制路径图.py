# -*- coding: cp936 -*-
# ��ϸ��P297
# �������,���ӻ�
# ����·��ͼ��ɢ��ͼ��ģ������˶�

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# ֻҪ�����ڻ״̬���Ͳ��ϵ�ģ���������
while True:
    # ����һ��RandomWalk��ʵ����ִ�л�ȡ300������ĵ�ķ���
    rw = RandomWalk(300)
    rw.fill_walk()

    # ���û�ͼ���ڵĳߴ�,ָ���ֱ���
    plt.figure(dpi=128, figsize=(10, 6))

    # ����·��ͼ,����Ϊ+�������㻮��-.
    plt.plot(rw.x_values, rw.y_values, linestyle='-.', linewidth=1, color='red', marker='+')

    # ͻ�������յ㣬��������ɢ��
    plt.scatter(0, 0, c='red', edgecolor='none', s=300)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow',
                edgecolor='none', s=300)

    # ����������
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # ���һ���������
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running == 'N':
        break




