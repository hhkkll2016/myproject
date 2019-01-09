#!/usr/bin/env python3
# - * - coding: UTF-8 - * -

  
import tushare as ts

cons = ts.get_apis()
"""
df = ts.bar('600547',conn=cons,freq='D',adj='qfq',start_date='2017-11-01',end_date='')
print(df)
"""

df = ts.tick('600547', conn=cons, date='2017-11-01')
df.head(20)
print(df)





