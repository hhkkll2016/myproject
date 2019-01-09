#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import numpy as np
import pandas as pd


dfStockListFromIndustry = ts.get_industry_classified() #select the communication and electronics industry
#dfStockListFromIndustry.to_csv(r'/Users/chenjuan/PycharmProjects/demo/001.csv')
#dfStockListFromIndustry[(dfStockListFromIndustry.c_name == '电子器件')|(dfStockListFromIndustry.c_name == '电子信息')]
def dataFilter(dfStock_List, *includinglist):
#select stocks by the dedicated industry
    n = 0
    boolValue = False
    for i in includinglist:
        boolValue = (dfStock_List.c_name == includinglist[n]) | boolValue
        n = n + 1
    dfStock_List = dfStock_List[boolValue]
    return dfStock_List
#get the list of stock code for '电子器件', '电子信息'
includingdata = list(dataFilter(dfStockListFromIndustry, '电子器件', '电子信息').code)
#get the list of stock code for '次新股'
excludingdata = list(dataFilter(dfStockListFromIndustry, '次新股').code)
def listFilter(list1, list2):
#delete the list menber existing in list2 from list1, return the list1
    for i in list2:
        for j in list1:
            if i == j:
                del list1[list1.index(j)]
    return list1
StockAfterIndustryFilter = listFilter(includingdata,excludingdata)


def dataFilterbyBsiscs (StockList):
#select the stock by the stock basic information
    dfStockListFromBasics = ts.get_stock_basics()
    #code,代码name,名称industry,所属行业area,地区pe,市盈率outstanding,流通股本(亿)totals,总股本(亿)
    #totalAssets,总资产(万)liquidAssets,流动资产fixedAssets,固定资产reserved,公积金reservedPerShare,每股公积金
    #esp,每股收益bvps,每股净资pb,市净率timeToMarket,上市日期undp,未分利润perundp, 每股未分配rev,收入同比(%)
    #profit,利润同比(%)gpr,毛利率(%)npr,净利润率(%)holders,股东人数
    #市盈率大于0小于40，收入同比大于0，利润同比大于0.05，毛利率大于平均，市净率大于平均
    GPReverage = 0.1
    NPReverage = 0.1
    dfStockListFromBasics_1 = dfStockListFromBasics[(dfStockListFromBasics.pe>0) & (dfStockListFromBasics.pe<65) \
                                                    & (dfStockListFromBasics.rev>0) \
                                                    & (dfStockListFromBasics.profit>0)\
                                                    & (dfStockListFromBasics.gpr>GPReverage)\
                                                    & (dfStockListFromBasics.npr>NPReverage)]
    dfStockListFromBasics_1 = dfStockListFromBasics_1[dfStockListFromBasics_1.index.isin(StockList)]
    StockAfterBasicsFilter = list(dfStockListFromBasics_1.index)
    return StockAfterBasicsFilter
StockAfterBasicsFilter = dataFilterbyBsiscs(StockAfterIndustryFilter)



print(StockAfterBasicsFilter)




#dfStockListFromConcept = ts.get_concept_classified() #excluding the second new stock
#dfStockListFromConcept.to_csv(r'/Users/chenjuan/PycharmProjects/demo/002.csv')