#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import numpy as np
import pandas as pd
import time,datetime

"""
ToDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
FromDate = time.strftime('%Y-%m-%d',time.localtime(time.time()-1.5*365*24*60*60))
dfForHistoryData = ts.get_hist_data('002281',start=FromDate,end=ToDate)
#code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
#start：开始日期，格式YYYY-MM-DD
#end：结束日期，格式YYYY-MM-DD
#ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
#retry_count：当网络异常后重试次数，默认为3
#pause:重试时停顿秒数，默认为0
#outputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutputoutput
#date：日期open：开盘价high：最高价close：收盘价low：最低价volume：成交量price_change：价格变动p_change：涨跌幅ma5：5日均价
## ma10：10日均价ma20:20日均价v_ma5:5日均量v_ma10:10日均量v_ma20:20日均量turnover:换手率[注：指数无此项]

print(dfForHistoryData[['close','volume']])


##today = datetime.date.today()
##benchmarkday = datetime.date.today()- datetime.timedelta(days=1)
##before61days = benchmarkday - datetime.timedelta(days=61)
##before180days = benchmarkday - datetime.timedelta(days=180)
##print(today,benchmarkday,before61days,before180days)


end_date = '2008-12-31'
period = 30

end_date = pd.Timestamp(end_date)
start_date = end_date - pd.Timedelta(days=period)

print(end_date,start_date)
"""
#获取tushre新接口数据连接
cons =ts.get_apis()

#给定一个时间基准
today = datetime.date.today()
benchmarkday = datetime.date.today()- datetime.timedelta(days=1)
before61days = benchmarkday - datetime.timedelta(days=61)
before180days = benchmarkday - datetime.timedelta(days=180)
print(ts.bar("600982",conn=cons,freq='D',adj='qfq',start_date=before61days,end_date=benchmarkday))
