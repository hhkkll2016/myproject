#!/user/bin/env python3
# - * - coding:UTF-8 - * -

import tushare as ts



df = ts.get_hist_data("000938")
print(df)

##df = ts.get_deposit_rate()
##print(df)
