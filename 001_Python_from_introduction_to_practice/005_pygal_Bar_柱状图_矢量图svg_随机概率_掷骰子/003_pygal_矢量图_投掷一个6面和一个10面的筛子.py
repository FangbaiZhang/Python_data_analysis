# -*- coding: cp936 -*-
# ��ϸ��P309
# Ͷ��������ͬ�������

import pygal
from die import Die

# ����һ��D6��һ��D10ʵ��
die_1 = Die()
die_2 = Die(10)

# Ͷ���������ӣ���������洢��һ���б���
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# ��������������ֳ��ֵ�����
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    # count��������ͳ��һ��ֵ���б��г��ֵĴ���
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# �Խ�����п��ӻ�

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."

hist.x_labels = list(range(2, 17))
print(hist.x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('003_pygal_ʸ��ͼ_Ͷ��һ��6���һ��10���ɸ��.svg')





