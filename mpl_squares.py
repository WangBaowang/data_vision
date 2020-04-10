# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 9:07
# 文件名称: mpl_squares.py
# 开发工具: PyCharm
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()