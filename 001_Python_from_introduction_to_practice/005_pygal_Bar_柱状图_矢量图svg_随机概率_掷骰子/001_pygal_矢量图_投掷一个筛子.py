# -*- coding: cp936 -*-
# ��ϸ��P305
# Ͷ�����ӣ�ͳ��ÿһ����ֵ�Ƶ�ʣ���״ͼ���ӻ�

import pygal
from die import Die

# ����һ��D6ʵ������������Ͷ��ɸ��
die = Die()

# Ͷ���������ӣ���������洢��һ���б���
results = []
for roll_num in range(1000):
    # roll����Ͷ��һ��ɸ�ӣ�����Ͷ��һ�εĽ��
    result = die.roll()
    results.append(result)

# ��������������ֳ��ֵ�����
frequencies = []
for value in range(1, die.num_sides + 1):
    # count��������ͳ��һ��ֵ���б��г��ֵĴ���
    frequency = results.count(value)
    frequencies.append(frequency)
# ��ӡ��ÿһ����ֵĴ���
print(['1', '2', '3', '4', '5', '6'])
print(frequencies)

# �Խ�����п��ӻ�������һ����ͼʵ������������ͼ
hist = pygal.Bar()

# ���ñ���
hist.title = "Results of rolling one D6 1000 times."
# ����X��������
hist.x_labels = ['1', '2', '3', '4', '5', '6']
# ����X�����
hist.x_title = "Result"
# ����Y�����
hist.y_title = "Frequency of Result"
# ���Y�����ݼ�˵��
hist.add('D6', frequencies)
# ���ʸ��ͼ�Σ������������
hist.render_to_file('001_pygal_ʸ��ͼ_Ͷ��һ��ɸ��.svg')





