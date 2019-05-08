# -*- coding: cp936 -*-
# ��ϸ��P305
# Ͷ����������,���ֵ�Ƶ�ʣ�����ĳЩ���ֳ��ֵ���࣬
# ��Ϊ����ɸ�Ӿʹ���ĳЩ��ϵ����⣬���Ϊ7��������

import pygal
from die import Die

# ����������D6ʵ��
die_1 = Die()
die_2 = Die()

# Ͷ���������ӣ���������洢��һ���б���
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# ��������������ֳ��ֵ�����
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    # count��������ͳ��һ��ֵ���б��г��ֵĴ���
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# �Խ�����п��ӻ�,����һ����ͼʵ��
hist = pygal.Bar()
# ���ñ���
hist.title = "Results of rolling one D6 1000 times."
# ��ȡX���ֵ
hist.x_labels = []
for x in range(2, 13):
    hist.x_labels.append(x)
print(hist.x_labels)
# ����X��������
hist.x_title = "Result"
# ����Y�����
hist.y_title = "Frequency of Result"
# ���Y�����ݼ�˵��
hist.add('D6 + D6', frequencies)
# ���ʸ��ͼ�Σ������������
hist.render_to_file('002_pygal_ʸ��ͼ_Ͷ������ɸ��.svg')





