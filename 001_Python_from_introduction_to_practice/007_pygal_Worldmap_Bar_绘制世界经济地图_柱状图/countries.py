# -*- coding: cp936 -*-
# ��ϸ��P327
# ��������룬��ӡ�������룬����Ѱ�ҹ�����
# pygal��ʹ�õĹ��Ҵ���洢���ֵ�COUNTRIES

from pygal_maps_world.i18n import COUNTRIES

# ����ĸ˳����������б�Ȼ���ӡ���Ҵ���͹�������
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

 

