#!/usr/bin/pathon
# __*__ coding: UTF-8 __*__

import tushare as ts
import matplotlib.pyplot as plt
import talib as ta
import numpy as np
import pandas as pd
import os,time,sys,re,datetime
import csv
import scipy
import datetime
import time

df600547 = ts.get_k_data('600547')

macd, macdsignal, macdhist = ta.MACD(np.array(df600547['close']), \
                                     fastperiod=12, \
                                     slowperiod=26, \
                                     signalperiod=9)
SignalMA5 = ta.MA(macdsignal, timeperiod=5, matype=0)
SignalMA10 = ta.MA(macdsignal, timeperiod=10, matype=0)
SignalMA20 = ta.MA(macdsignal, timeperiod=20, matype=0)
df600547['macd']=pd.Series(macd,index=df600547.index) #DIFF
df600547['macdsignal']=pd.Series(macdsignal,index=df600547.index)#DEA
df600547['macdhist']=pd.Series(macdhist,index=df600547.index)#DIFF-DEA


x = []

for i in df600547["date"]:
    i = datetime.datetime.strptime(i,'%Y-%m-%d')
    x.append(i)
    

##plt.gca().xaxis.set_major_formatter(x.DateFormatter('%m/%d/%Y'))
##plt.gca().xaxis.set_major_locator(x.DayLocator())

plt.plot(x,df600547["close"])
plt.plot(x,df600547["macd"])
plt.plot(x,df600547["macdsignal"])
plt.plot(x,df600547["macdhist"])

plt.gcf().autofmt_xdate()  # 自动旋转日期标记

#设置标题，横坐标标签，纵坐标标签
plt.title('daily data')
plt.xlabel('date')
plt.ylabel('closed price')

plt.show()

"""
print(df600547)

"""



