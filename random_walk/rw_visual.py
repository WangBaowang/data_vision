# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 10:31
# 文件名称: rw_visual.py
# 开发工具: PyCharm
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='None', s=1)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors="None", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors="None", s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break