# -*- coding: cp936 -*-
# ��ϸ��P296
# ����һ�������������

from random import choice


class RandomWalk():
    """һ�����������������"""

    def __init__(self, num_points=50):
        """��ʼ���������������"""
        self.num_points = num_points

        # ���������������ʼ�ڣ�0,0��
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """��������������������еĵ�"""

        # ����������ֱ���б���ָ���ĳ���
        while len(self.x_values) < self.num_points:
            # ����ǰ�������Լ����������ǰ���ľ���
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
            y_step = y_direction * y_distance

            # �ܾ�ԭ��̤��
            if x_step == 0 and y_step == 0:
                continue

            # ������һ�����x��yֵ,��Ƭ[-1]Ϊ�б�����һ��ֵ��
            # ��ʼ���ǣ�0,0������һ��ѭ��x��2��y��3������0+2,0+3
            # �õ��ڶ����㣨2,3��
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # ��ÿ�εõ�һ�����x,y������뵽�б���
            self.x_values.append(next_x)
            self.y_values.append(next_y)




