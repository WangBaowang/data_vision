# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 15:08
# 文件名称: matplotlib_die.py
# 开发工具: PyCharm
import matplotlib.pyplot as plt

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

plt.hist(results, die_1.num_sides+die_2.num_sides-1)

plt.title('Results of rolling a D6 and a D6 1000 times.')
plt.xlabel('Result')
plt.ylabel('Frequency of Result')

plt.show()