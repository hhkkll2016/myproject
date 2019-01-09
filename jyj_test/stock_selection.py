#!/usr/bin/env python3

"""This script parse stock info"""  
  
import tushare as ts  

df = ts.get_concept_classified()

df.to_csv("c:/proj_stock/df1.csv")

"""
ds_jbm_gplb = ts.get_stock_basics()   #基本面_股票列表
ds_jbm_gplb.to_csv("c:/proj_stock/ds_jbm_gplb.csv")

ds_jbm_yjbg=ts.get_report_data(2016,3)  #基本面_业绩报告,按照年度和季度
ds_jbm_yjbg.to_csv("c:/proj_stock/ds_jbm_yjbg.csv")

ds_jbm_ylnl=ts.get_profit_data(2016,3)  #基本面_盈利能力,按照年度和季度
ds_jbm_ylnl.to_csv("c:/proj_stock/ds_jbm_ylnl.csv")

ds_jbm_yynl=ts.get_operation_data(2016,3)    #基本面_营运能力,按照年度和季度
ds_jbm_yynl.to_csv("c:/proj_stock/ds_jbm_yynl.csv")

ds_jbm_cznl=ts.get_growth_data(2016,3)    #基本面_成长能力,按照年度和季度
ds_jbm_cznl.to_csv("c:/proj_stock/ds_jbm_cznl.csv")

ds_jbm_czainl=ts.get_debtpaying_data(2016,3)    #基本面_偿债能力,按照年度和季度
ds_jbm_czainl.to_csv("c:/proj_stock/ds_jbm_czainl.csv")

ds_jbm_xjll=ts.get_cashflow_data(2016,3)    #基本面_现金流量,按照年度和季度
ds_jbm_xjll.to_csv("c:/proj_stock/ds_jbm_xjll.csv")

ds_industry_classified=ts.get_industry_classified()   #分类_行业分类
ds_industry_classified.to_csv("c:/proj_stock/ds_industry_classified.csv")

ds_concept_classified=ts.get_concept_classified()   #分类_概念分类
ds_concept_classified.to_csv("c:/proj_stock/ds_concept_classified.csv")

ds_new_ipo=ts.new_stocks(retry_count=3,pause=0)   #IPO数据
ds_new_ipo.to_csv("c:/proj_stock/ds_new_ipo.csv")


"""








