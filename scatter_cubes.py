# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 9:46
# 文件名称: scatter_cubes.py
# 开发工具: PyCharm
import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolors='None', s=40)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 5100, 0, 130000000000])

plt.show()