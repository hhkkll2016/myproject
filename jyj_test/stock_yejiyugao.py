#!/usr/bin/env python3

"""This script parse stock info"""  
  
import tushare as ts  


ds_ck_fpya = ts.profit_data(year=2017, top=100)   #分配预案
#参数说明：
#•year : 预案公布的年份，默认为2014
#•top :取最新n条数据，默认取最近公布的25条
#•retry_count：当网络异常后重试次数，默认为3
#•pause:重试时停顿秒数，默认为0

#返回值说明：
#•code:股票代码
#•name:股票名称
#•year:分配年份
#•report_date:公布日期
#•divi:分红金额（每10股）
#•shares:转增和送股数（每10股）
ds_ck_fpya.sort_values(by = 'shares', ascending = False)
ds_ck_fpya.to_csv("c:/proj_stock/ds_ck_fpya.csv")

"""

ds_ck_yjyg = ts.forecast_data(2016, 4)   #业绩预告
#参数说明：
#•year:int 年度 e.g:2014
#•quarter:int 季度 :1、2、3、4，只能输入这4个季度
#结果返回的数据属性说明如下：
#code,代码
#name,名称
#type,业绩变动类型【预增、预亏等】
#report_date,发布日期
#pre_eps,上年同期每股收益
#range,业绩变动范围
ds_ck_yjyg.to_csv("c:/proj_stock/ds_ck_yjyg.csv")

"""









