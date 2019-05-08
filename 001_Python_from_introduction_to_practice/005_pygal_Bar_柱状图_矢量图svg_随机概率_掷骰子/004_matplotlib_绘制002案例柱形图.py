# -*- coding: cp936 -*-
# ��ϸ��P309
# Ͷ��������ͬ������ӣ�����matplotlib.pyplot��������ͼ

import matplotlib.pyplot as plt
from die import Die

# ����һ��D6��һ��D6ʵ��
die_1 = Die()
die_2 = Die()

# Ͷ���������ӣ���������洢��һ���б���
results = []
for roll_num in range(500):
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
print(list(range(2, 13)))

# �Խ�����п��ӻ�,ʹ��matplotlib��������ͼ
x_labels = list(range(2, 13))
plt.bar(range(2, 13), frequencies, color='rgb', tick_label=range(2, 13))
plt.show()




