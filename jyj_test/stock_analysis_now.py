#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
#import numpy as np
#import pandas as pd
#import time

#Today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
dfForTodayDeal = ts.get_today_ticks('002281')
#outputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutput
#time：时间price：当前价格pchange:涨跌幅change：价格变动volume：成交手amount：成交金额(元)type：买卖类型【买盘、卖盘、中性盘】
#TotalPriceForBuy = dfForTodayDeal[(dfForTodayDeal.type == '买盘')].assign(totalprice = lambda x: (x['price']*x['volume']*100))
TotalAmount = dfForTodayDeal.sum()['amount'] - dfForTodayDeal[(dfForTodayDeal['type'] == 0)].sum()['amount']
TotalAmountForBuy = dfForTodayDeal[(dfForTodayDeal['type'] == '买盘')].sum()['amount']
TotalAmountForSale = dfForTodayDeal[(dfForTodayDeal['type'] == '卖盘')].sum()['amount']
TotalAmountForNeutral = dfForTodayDeal[(dfForTodayDeal['type'] == '中性盘')].sum()['amount']
print('\n','交易总额：%d;  买盘总额：%d；卖盘总额：%d；中性盘总额：%d' \
      %(TotalAmount,TotalAmountForBuy,TotalAmountForSale,TotalAmountForNeutral))
#print(TotalAmountForBuy)
#dfForTodayDeal.to_csv(r'/Users/chenjuan/PycharmProjects/demo/003.csv')
