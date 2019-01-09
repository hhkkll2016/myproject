#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts


df_film = ts.realtime_boxoffice()
print(df_film)

df_film_date = ts.day_boxoffice('2017-05-17')
print(df_film_date)