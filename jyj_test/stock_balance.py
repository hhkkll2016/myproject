#!/usr/bin/env python3

"""This script parse stock info"""  
  
import tushare as ts  


#ds_balance = ts.get_balance_sheet('000998')   #资产负债表

#ds_balance.to_csv("c:/proj_stock/ds_balance.csv")

ds_news = ts.get_latest_news(show_content = 'True')

ds_news.to_csv("c:/proj_stock/ds_news.csv")









