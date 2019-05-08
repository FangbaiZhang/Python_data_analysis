# -*- coding: cp936 -*-
# 详细见P327
# 导入国别码，打印出国别码，用于寻找国别码
# pygal中使用的国家代码存储在字典COUNTRIES

from pygal_maps_world.i18n import COUNTRIES

# 按字母顺序遍历国家列表，然后打印国家代码和国家名称
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

 

