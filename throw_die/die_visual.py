# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 11:34
# 文件名称: die_visual.py
# 开发工具: PyCharm
import pygal

from die import Die

# 创建一个D6
die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(1, die.num_sides+1))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('C:/Users/baowang/Desktop/frequencies.svg')    # 可在浏览器打开，有交互