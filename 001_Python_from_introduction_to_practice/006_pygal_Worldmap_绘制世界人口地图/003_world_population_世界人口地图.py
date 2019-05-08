# -*- coding: cp936 -*-
# ��ϸ��P325
# ����JSON�ļ�

import json
import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS


# �����ݼ��ص�һ���б���
filename = 'population_data.json'
with open(filename) as f:
    # ��ȡ�ļ��е����ݣ���ȡ�Ľ��Ϊһ���б��б���ÿһ��Ԫ�ض���һ���ֵ�
    pop_data = json.load(f)
    

# ����һ������ÿ�������˿��������ֵ�
cc_population = {}
# �����б��е�ÿһ���ֵ䣬������һ�����Ҳ�ͬ��ݵ����ݣ�ѡȡ2010��ݵ�����
for pop_dict in pop_data:
    # ����ݶ�Ӧ��ֵ�Ƿ�Ϊ2010��ԭʼ����2010Ϊ�ַ��������Զ����ַ����Ƚ�
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # ����ԭʼ�����д���С�����Ƚ�����ת��Ϊ��������Ȼ��ת��������
        population = int(float(pop_dict['Value']))
        # pygalֻ��ʹ��������ĸ�Ĺ����룬JSON���ṩ����3λ�ģ�����һ���������2λ�Ĺ�����
        code = get_country_code(country_name)
        if code:
            # �����������ڣ�����������Ϊ�����˿�������Ϊֵ���洢���ֵ���
            cc_population[code] = population
        else:
            # ��������Щ����������д�ĺ�pygal��ʽ��һ�£���Ȼ�����ݣ����ǲ��ܻ�ù����룬��ӡһ����ʾ��Ϣ
            print('ERROR - ' + country_name)

# �����˿����������еĹ��ҷ���
cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 100000000:
        cc_pops_2[cc] = pop
    elif pop < 1000000000:
        cc_pops_3[cc] = pop
    else:
        cc_pops_4[cc] = pop

# ����ÿ������������ٸ�����
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3), len(cc_pops_4))

# ����ÿ�������Ӧ����ɫ������33��ɫ��66��ɫ��99��ɫ
# base_style=LCS�������ڼ�����ͼ����ɫ����ΪpygalĬ�ϵ��ǽϰ�����ɫ����
wm_style = RS('#336699', base_style=LCS)
# ���������Զ���ĵ�ͼ��ʾ���
wm = pygal_maps_world.maps.World(style=wm_style)
# ���ñ���
wm.title = 'World Population in 2010, by Country'
# ���ÿ����ǩ�����Ӧ�Ĺ����˿ڵ�����
wm.add('0-10m', cc_pops_1)
wm.add('10m-100m', cc_pops_2)
wm.add('100m-1bn', cc_pops_3)
wm.add('>1bn', cc_pops_4)

# ����ļ�
wm.render_to_file('003_world_population_�����˿ڵ�ͼ.svg')
 

