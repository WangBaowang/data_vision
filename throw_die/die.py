# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 11:30
# 文件名称: die.py
# 开发工具: PyCharm
from random import randint

class Die():
    '''表示一个骰子的类'''
    def __init__(self, num_sides=6):
        '''骰子默认为6面'''
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)