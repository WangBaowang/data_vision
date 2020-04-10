# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/4/5 16:01
# 文件名称: highs_lows.py
# 开发工具: PyCharm
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_1 = 'sitka_weather_2014.csv'
filename_2 = 'death_valley_2014.csv'
with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_head in enumerate(header_row):
    #     print(index, column_head)

    dates_1, highs_1, lows_1= [], [], []
    for row in reader:
        try:
            current_time = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_time, 'missing data')
        else:
            dates_1.append(current_time)
            highs_1.append(high)
            lows_1.append(low)

with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_head in enumerate(header_row):
    #     print(index, column_head)

    dates_2, highs_2, lows_2= [], [], []
    for row in reader:
        try:
            current_time = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_time, 'missing data')
        else:
            dates_2.append(current_time)
            highs_2.append(high)
            lows_2.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# 给图表区域着色:alpha(透明度)
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_1, lows_1, c='blue', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

plt.plot(dates_2, highs_2, c='yellow', alpha=0.5)
plt.plot(dates_2, lows_2, c='green', alpha=0.5)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='pink', alpha=0.1)


# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()    # 斜日期绘制
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()