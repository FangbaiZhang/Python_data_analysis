# -*- coding: cp936 -*-
# ����һϵ�е��ɢ��ͼ���Զ��������ݣ������õ����ɫ�ͱ�Եɫ
# ��ϸ��P292

import matplotlib.pyplot as plt

# �Զ���������
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# ��ͼ�����õ�Ĵ�С����ɫ�ͱ�Եɫ
plt.scatter(x_values, y_values, c='blue', edgecolor='red', s=30)
# ʹ��RGB����ͼ����ɫ,������ɫc����0-1��ֵ���ֱ��ʾ��������ֵΪ1,0,0���Ǻ�ɫ
# plt.scatter(x_values, y_values, c=(1, 0, 0), edgecolor='red', s=30)

# ����ͼ����Ⲣ����������ϱ�ǩ
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# ���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', which='both', colors='blue', labelsize=14)

# ����ÿ���������ȡֵ��Χ
plt.axis([0, 50, 0, 2500])

plt.show()

