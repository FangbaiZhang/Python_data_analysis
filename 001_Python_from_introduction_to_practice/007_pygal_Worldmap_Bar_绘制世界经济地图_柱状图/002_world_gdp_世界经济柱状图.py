# -*- coding: cp936 -*-
# ��ϸ��P325
# ����JSON�ļ�

import json 
import pygal
from country_codes import get_country_code
from pygal.style import LightColorizedStyle , RotateStyle


filename = 'world_gdp.json'

with open(filename) as f:
    pop_data = json.load(f)
    
world_gdp = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        gdp = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            # �����������ڣ�����������Ϊ�����˿�������Ϊֵ���洢���ֵ���
            world_gdp[country_name] = gdp
# print(world_gdp)

# ��GDP����ֵ����
low_gdp_name, medium_gdp_name, high_gdp_name, super_gdp_name = [], [], [], []
low_gdp, medium_gdp, high_gdp, super_gdp = [], [], [], []

for cn, gp in world_gdp.items():
    # gdp̫�ٵ�ֱ�Ӻ��Ե�����Ϊ��������ͼ�ϣ�������̫С��ʾ������
    # ���ҹ���̫����,X��ܴ�һ���ֶ��ǿ����ǿհ׵�
    if gp < 15000*100000000:
        print()
    elif gp < 20000*100000000:
        low_gdp_name.append(cn)
        low_gdp.append(gp)
    elif gp < 30000*100000000:
        medium_gdp_name.append(cn)
        medium_gdp.append(gp)
    elif gp < 50000*100000000:
        high_gdp_name.append(cn)
        high_gdp.append(gp)
    else:
        super_gdp_name.append(cn)
        super_gdp.append(gp)

print(low_gdp_name)
print(medium_gdp_name)
print(high_gdp_name)
print(super_gdp_name)

# ��ͬϵ�в��ò�ͬ����ɫ
# ��һ��������16���Ƶ�RGB��ɫ��ǰ��λ����R���м���λ����G�������λ����B��
# ����Խ����ɫԽ��ڶ����������û�����ʽΪ��ɫ���⣬pygalĬ��ʹ�ýϰ�����ɫ����
bar_style = RotateStyle('#336699', base_style=LightColorizedStyle)

bar = pygal.Bar(style=bar_style)

bar.title = 'World GDP in 2016'

bar.add('LOW_GDP', low_gdp)
bar.add('MEDIUM_GDP', medium_gdp)
bar.add('HIGH_GDP', high_gdp)
bar.add('SUPER_GDP', super_gdp)

bar.x_title = 'Country Name'
bar.y_title = 'GDP of Country'
bar.render_to_file('002_world_gdp_���羭����״ͼ.svg')

 

