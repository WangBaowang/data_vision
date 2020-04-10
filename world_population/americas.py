# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/6 15:34
# 文件名称: americas.py
# 开发工具: PyCharm

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()

wm.title = 'North, Central, and South America'
wm.add('North America', {'ca': 34126000, 'mx':113423000, 'us':309349000})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('C:/Users/baowang/Desktop/americas.svg')
