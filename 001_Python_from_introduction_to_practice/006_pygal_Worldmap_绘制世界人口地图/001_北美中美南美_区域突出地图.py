# -*- coding: cp936 -*-
# ��ϸ��P329
# ������������_����ͻ����ͼ
# ���Ǹ������������ͻ����ʾ�����ͼ���еı�ǩ�������ر�ǩ��Ӧ�ĵ�ͼ�����ڵ�ͼ�ϻ��Զ���ʾ���ҵ�����

import pygal_maps_world.maps

# ����һ����ͼ����ʵ��
# pygal_maps_world.maps.World()��ר�����ڻ��Ƶ�ͼ
# ����������ָ�ʽ��ͼ��
wm = pygal_maps_world.maps.World()

# ����ͼ�α���
wm.title = 'North, Central, and South America'
# add��������һ����ǩ���б���һ���ǲ�����˵����ǩ���ڶ����б��������Ҫͻ���Ĺ�����
# �����ͬһ��add�еĹ�Ϊһ�࣬����ͬ�ı�ǩ����ɫ
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

# ���ʸ��ͼ��������򿪣����ͼ���еı�ǩ�������ر�ǩ��Ӧ�ĵ�ͼ�����ڵ�ͼ�ϻ��Զ���ʾ���ҵ�����
wm.render_to_file('001_������������_����ͻ����ͼ.svg')
