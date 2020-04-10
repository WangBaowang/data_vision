# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 12:07
# 文件名称: different_dice.py
# 开发工具: PyCharm
import pygal

from die import Die

def diff_dice(*d, t=1000):
    '''

    投多个骰子
    :param t: 投掷次数
    :param d: 骰子点数
    :return:
    '''
    # 创建骰子
    max_result = 0
    for i in range(len(d)):
        die_i = Die(d[i])
        max_result += die_i.num_sides

    # 掷骰子多次，并将结果存在一个列表中
    results = []
    for roll_num in range(t):
        result = 0
        for i in range(len(d)):
            result += die_i.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    min_result = len(d)
    for value in range(min_result, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # 可视化结果
    hist = pygal.Bar()

    hist.title = f"Results of rolling {len(d)} dice {t} times."
    hist.x_labels = list(range(min_result, max_result+1))
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    hist.add(f'{len(d)} dice', frequencies)
    hist.render_to_file(f'C:/Users/baowang/Desktop/{len(d)}_diff_dice.svg')

diff_dice(*(6, 6, 6), t=50000)