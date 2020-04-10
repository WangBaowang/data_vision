# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/6 11:09
# 文件名称: world_population.py
# 开发工具: PyCharm
import json
import pygal_maps_world.maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# wm_style = RS('#336699', base_style=LCS)    # 十六进制的RGB颜色
# wm = pygal_maps_world.maps.World(style=wm_style)
wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('> 1bn', cc_pops_3)

wm.render_to_file('C:/Users/baowang/Desktop/world_population.svg')