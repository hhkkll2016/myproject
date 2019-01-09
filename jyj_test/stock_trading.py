#!/usr/bin/env python3

"""This script parse stock info"""  
  
import tushare as ts
import os
import datetime




#统计一段时间某一只股票的大单成交量
def datelist(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
        curr_date += datetime.timedelta(1)
    result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
    return result

#if __name__ == "__main__":
#print (datelist((2014, 7, 28), (2014, 8, 3)))

datelist_for_ddjy = datelist((2017,3,20),(2017,3,24))  #不能含有休市日期
filename = 'c:/proj_stock/ds_hq_ddjy.csv'
for date_jiaoyi in  datelist_for_ddjy:
    ds_hq_ddjy = ts.get_sina_dd('002027',date = date_jiaoyi, vol = 200)
    if os.path.exists(filename):
        ds_hq_ddjy.to_csv(filename, mode = 'a', header = None)
    else:
        ds_hq_ddjy.to_csv(filename)



"""

ds_hq_lshq = ts.get_hist_data('sh')   #历史行情
#只能获取近3年的日线数据,全部历史数据get_h_data()。
#参数说明：
#•code：股票代码，即6位数字代码，或者指数代码
#（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
#•start：开始日期，格式YYYY-MM-DD
#•end：结束日期，格式YYYY-MM-DD
#•ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
#•retry_count：当网络异常后重试次数，默认为3
#•pause:重试时停顿秒数，默认为0
#返回值说明：
#•date：日期
#•open：开盘价
#•high：最高价
#•close：收盘价
#•low：最低价
#•volume：成交量
#•price_change：价格变动
#•p_change：涨跌幅
#•ma5：5日均价
#•ma10：10日均价
#•ma20:20日均价
#•v_ma5:5日均量
#•v_ma10:10日均量
#•v_ma20:20日均量
#•turnover:换手率[注：指数无此项]
ds_hq_lshq.to_csv("c:/proj_stock/ds_hq_lshq.csv")

ds_hq_lssj = ts.get_h_data('002281')   #复权数据
#可以获取全部数据，注意分年段获取
#参数说明：
#•code:string,股票代码 e.g. 600848
#•start:string,开始日期 format：YYYY-MM-DD 为空时取当前日期
#•end:string,结束日期 format：YYYY-MM-DD 为空时取去年今日
#•autype:string,复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
#•index:Boolean，是否是大盘指数，默认为False
#•retry_count : int, 默认3,如遇网络等问题重复执行的次数
#•pause : int, 默认 0,重复请求数据过程中暂停的秒数
#返回值说明：
#•date : 交易日期 (index)
#•open : 开盘价
#•high : 最高价
#•close : 收盘价
#•low : 最低价
#•volume : 成交量
#•amount : 成交金额
ds_hq_lssj.to_csv("c:/proj_stock/ds_hq_lssj.csv")

ds_hq_allhq = ts.get_today_all( )   #实时行情
#一次性获取当前交易所有股票的行情数据
#code：代码
#•name:名称
#•changepercent:涨跌幅
#•trade:现价
#•open:开盘价
#•high:最高价
#•low:最低价
#•settlement:昨日收盘价
#•volume:成交量
#•turnoverratio:换手率
#•amount:成交量
#•per:市盈率
#•pb:市净率
#•mktcap:总市值
#•nmc:流通市值
ds_hq_allhq.to_csv("c:/proj_stock/ds_hq_allhq.csv")


ds_hq_lsfb = ts.get_tick_data('002281',data = '2017-03-23' )   #历史分笔
#ds_hq_lsfb.head (10) #取最近几笔
#参数说明：
#•code：股票代码，即6位数字代码
#•date：日期，格式YYYY-MM-DD
#•retry_count : int, 默认3,如遇网络等问题重复执行的次数
#•pause : int, 默认 0,重复请求数据过程中暂停的秒数
#返回值说明：
#•time：时间
#•price：成交价格
#•change：价格变动
#•volume：成交手
#•amount：成交金额(元)
#•type：买卖类型【买盘、卖盘、中性盘】
ds_hq_lsfb.to_csv("c:/proj_stock/ds_hq_lsfb.csv")


ds_hq_ssfb = ts.get_realtime_quotes('002281')   #实时分笔
#ds_hq_ssfb = ts.get_realtime_quotes(['002281','sh','600848'])   #返回多个
#ds_hq_ssfb(['code','name','price'])  #取部分返回字段
#参数说明：
#•symbols：6位数字股票代码，或者指数代码
#返回值说明：
#0：name，股票名字
#1：open，今日开盘价
#2：pre_close，昨日收盘价
#3：price，当前价格
#4：high，今日最高价
#5：low，今日最低价
#6：bid，竞买价，即“买一”报价
#7：ask，竞卖价，即“卖一”报价
#8：volume，成交量 maybe you need do volume/100
#9：amount，成交金额（元 CNY）
#10：b1_v，委买一（笔数 bid volume）
#11：b1_p，委买一（价格 bid price）
#12：b2_v，“买二”
#13：b2_p，“买二”
#14：b3_v，“买三”
#15：b3_p，“买三”
#16：b4_v，“买四”
#17：b4_p，“买四”
#18：b5_v，“买五”
#19：b5_p，“买五”
#20：a1_v，委卖一（笔数 ask volume）
#21：a1_p，委卖一（价格 ask price）
#...
#30：date，日期；
#31：time，时间；
ds_hq_ssfb.to_csv("c:/proj_stock/ds_hq_ssfb.csv")


ds_hq_drlsfb = ts.get_tick_data('002281',data = '2017-03-23' )   #当日历史分笔
#ds_hq_drlsfb.head (10) #取最近几笔
#参数说明：
#•code：股票代码，即6位数字代码
#•retry_count : int, 默认3,如遇网络等问题重复执行的次数
#•pause : int, 默认 0,重复请求数据过程中暂停的秒数
#返回值说明：
#•time：时间
#•price：当前价格
#•pchange:涨跌幅
#•change：价格变动
#•volume：成交手
#•amount：成交金额(元)
#•type：买卖类型【买盘、卖盘、中性盘】
ds_hq_drlsfb.to_csv("c:/proj_stock/ds_hq_drlsfb.csv")

ds_hq_dphq = ts.get_index()   #大盘行情指数
#返回值说明：
#•code:指数代码
#•name:指数名称
#•change:涨跌幅
#•open:开盘点位
#•preclose:昨日收盘点位
#•close:收盘点位
#•high:最高点位
#•low:最低点位
#•volume:成交量(手)
#•amount:成交金额（亿元）
ds_hq_dphq.to_csv("c:/proj_stock/ds_hq_dphq.csv")

ds_hq_ddjy = ts.get_sina_dd('002281',data = '2017-03-23', vol = '400')   #大单交易数据
#参数说明：
#•code：股票代码，即6位数字代码
#•date:日期，格式YYYY-MM-DD
#•vol:手数，默认为400手，输入数值型参数
#•retry_count : int, 默认3,如遇网络等问题重复执行的次数
#•pause : int, 默认 0,重复请求数据过程中暂停的秒数
#返回值说明：
#•code：代码
#•name：名称
#•time：时间
#•price：当前价格
#•volume：成交手
#•preprice ：上一笔价格
#•type：买卖类型【买盘、卖盘、中性盘】
ds_hq_ddjy.to_csv("c:/proj_stock/ds_hq_ddjy.csv")

"""

