# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/6 15:27
# 文件名称: country_codes.py
# 开发工具: PyCharm

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    else:
        return country_name[0:2].lower()


# print(get_country_code("China"))
# print(get_country_code("Chine"))