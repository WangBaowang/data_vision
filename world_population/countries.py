# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/6 11:27
# 文件名称: countries.py
# 开发工具: PyCharm

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])