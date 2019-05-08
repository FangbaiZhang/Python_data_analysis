# -*- coding: cp936 -*-
# ��ϸ��P313
# ����CSV�ļ���CSV�ļ���һ��������EXCEL��񣬵�һ���Ǳ�ͷ���ݣ��ڶ��п�ʼ���Ƕ�Ӧ�ľ�������
# ��ȡ��ͷ���ݣ�������º���������������ڻ����¶�����ͼ

import csv
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

# ������ȡ2014��7�·ݵ���������
with open('death_valley_2014.csv') as f:
    # ��ȡ�����ļ������ݣ�ʹ��csvģ���е�reader,��ȡ�����һ���б�ÿһ����һ���б�
    reader = csv.reader(f)

    # ��ȡ�ļ��ĵ�һ�����ݣ�next����ÿ�ζ�ȡһ��,��ȡָ����ͣ
    header_row = next(reader)
    print(header_row)
    # ��ȡ�ڶ��е����ݣ��������������
    # second_row = next(reader)
    # print(second_row)
    # print()

    # ��ӡ�ļ�ͷ��ÿ�е����Ƽ���λ�ã�enumerate�������б���ÿ��Ԫ�����һ������
    # �������������������Ԫ�����һ��Ԫ�飬Ȼ�����е�Ԫ�����һ���µ��б�
    # ��ȡ��ÿ���б�Ԫ���е������Ͷ�Ӧ��ֵ
    for index, column_header in enumerate(header_row, start=1):
        print(index, column_header)
    print()

    # ���������ʾ��ȡ�ļ��е�������£����������ʾ����1��Ϊ���ڣ���2��Ϊ�������
    dates, highs, lows = [], [], []
    # �ӵ�2�п�ʼ����ÿһ�У���Ϊ��һ��ǰ���Ѿ�����next��ȡ��
    # ��ÿһ�е�һ�����ݣ��ڶ������ݣ����������ݣ����ں���ߺ����������ȡ��ӵ��б���
    for row in reader:
        # ��ȡ���ڣ�������£��������
        # ��Щ����ȱʧ����˼���try��䣬�ų�ȱʧ������
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# ���濪ʼ���ӻ��������
# �����������ݻ�����������ͼ,����ͼ�δ�С���ֱ���
fig = plt.figure(dpi=128, figsize=(7, 5))

# alpha����Ϊ͸���ȣ�0-1��ȡ1���ǲ�͸��
plt.plot(dates, highs, c='red', alpha=0.5, linewidth=2, ls='-')
plt.plot(dates, lows, c='blue', alpha=0.5, linewidth=1, ls='-')

# ����ͼ�����������ɫ
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

# ����ͼ�α��⣬X��Y�����
plt.title("Daily high temperature, July 2014\nDeath Valley, CA")
plt.xlabel("Date", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
# ��x�������б����ʾ
fig.autofmt_xdate()

# ��nump����Y������̶�
my_y_ticks = np.arange(0, 160, 10)
plt.yticks(my_y_ticks)

# ���ÿ̶ȣ�which����������ʾ�����̶ȣ��ô����ߵ�̫��û����������
# ���ÿ̶����ڲ�����ɫ��ɫ�Ȳ���
plt.tick_params(axis='both', which='both', width=2,
                colors='black', direction='in', labelsize=8)
# �����������ڣ���������y�������ȡֵ��Χ
# plt.ylim([0, 150])

plt.show()



