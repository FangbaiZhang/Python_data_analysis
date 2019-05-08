# -*- coding: cp936 -*-
# ��ϸ��P340
# ִ��API���ã��ҳ�GitHub��������ߵ���Ŀ

import requests

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
print("\nRepositories returned:", len(repo_dicts))

# �о���һ���ֿ⣬��ʵ�����о���һ���ֵ�
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
print()
# for key in sorted(repo_dict.keys()):
    # print(key)

# ��ǰ��һ���ֵ��еĹؼ���Ϣ
print("\nSelected information about first repository:")
# ֻ��ȡ�б��е�ǰ�����ֵ�
for repo_dict in repo_dicts[0:3]:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login']) # �ֵ����Ӧ��ֵ���ֵ䣬��ȡ���ֵ������ֵ
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    print()



 

