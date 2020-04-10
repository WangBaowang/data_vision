# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 15:24
# 文件名称: pygal_random_walk.py
# 开发工具: PyCharm
import pygal

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

xy_graph = pygal.XY(stroke=False)
xy_graph.add('Random_Walk', [(rw.x_values[i], rw.y_values[i]) for i in range(len(rw.x_values))])

xy_graph.render_to_file("C:/Users/baowang/Desktop/pygal_random_walk.svg")