# -*- coding: cp936 -*-
# ��ϸ��P329
# ���������ͼ���ڵ�ͼ����ʾ��������
# ��ʾ���������ҵ��˿�����

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Population of Countries in North America'
# ������ݣ���һ������Ϊ��ǩ˵������ʱ�ڶ����������ֵ䣬������Ͷ�Ӧ���˿�����
wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})

# ���ʸ��ͼ�ļ���������򿪣����ŵ������ϣ�����ʾ��ǩ˵�����������ƣ��˿�����
wm.render_to_file('002_����_����ͻ����ͼ_����˿�����.svg')
