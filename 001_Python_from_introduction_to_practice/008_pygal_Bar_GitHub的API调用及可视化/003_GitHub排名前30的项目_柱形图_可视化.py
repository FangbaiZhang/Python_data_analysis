# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-

# ��ϸ��P345
# ִ��API���ã��ҳ�GitHub��������ߵ�30����Ŀ

import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# ִ��API���ò��洢��Ӧ
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# ��ӡһ��״̬�룬��������ַ�Ƿ�ɹ�
print("Status code:", r.status_code)

# ��ȡ������ַ��Ϣ����ʵ����һ�������ֵ����Ϣ����API��Ӧ�洢��һ���ֵ���
response_dict = r.json()
# ������,��ӡ����ȡ�ĵ��ֵ��еļ�������ҳ�Աȣ�����û������
print(response_dict.keys())
print("Total repositories:", response_dict['total_count']) # ��ӡ����Ŀ

# ̽���йزֿ����Ϣ,items��Ӧ����һ���б��б��а����ܶ��ֵ�
repo_dicts = response_dict['items']

# ���ӻ��ֿ����Ϣ,���ֿ����ƺͶ�Ӧ������ȡ���б���
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        plot_dict={'value':repo_dict['stargazers_count'],
                   'label':repo_dict['description'],
                   'xlink':repo_dict['html_url']
                   }
        plot_dicts.append(plot_dict)
    else:
        plot_dict={'value':repo_dict['stargazers_count'],
                   'label':'ABC',
                   'xlink':repo_dict['html_url']}
        plot_dicts.append(plot_dict)
    
print(len(names))
print()
print(len(plot_dicts))
print()

my_style = LS('#993366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 30
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Python Projects'
chart.x_labels = names
chart.add('Star', plot_dicts)

chart.render_to_file('003_GitHub����ǰ30����Ŀ_����ͼ_���ӻ�.svg')





 

