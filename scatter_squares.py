# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 9:15
# 文件名称: scatter_squares.py
# 开发工具: PyCharm
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='pink', edgecolors='None', s=40)    # edgecolors 表示黑色轮廓，s 表示点的尺寸
# plt.scatter(x_values, y_values, c=(1, 0, 0), edgecolors='None', s=40)    # RGB取0-1之间的数
# 颜色映射，渐变
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors='None', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
# 自动保存可将plt.show()转化为下面的程序
# plt.savefig("C:/Users/baowang/Desktop/figure_compare.png", bbox_inches='tight')    # 第二个参数为裁剪掉空白区域