# -*- coding: cp936 -*-
# ��ϸ��P327
# ��дһ����ù��Ҵ����ģ��
# �˿�json�����У���Щ���ҵĹ������ǲ��õ���λ��Pygal��Ҫʹ��������ĸ��Ϊ������
# ��дһ�����������滻���еĲ��ֹ�����Ϊ��λ

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """����ָ���Ĺ��ң�����Pygalʹ�õ�������ĸ�Ĺ�����"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Vietnam':
            return 'vn'
    # ���û���ҵ�ָ���Ĺ��ң��ͷ���None
    return None



