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

df = ts.get_tick_data('002296',date='2017-09-18')
print(list(df['time']))
