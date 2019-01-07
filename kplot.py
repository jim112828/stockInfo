import numpy as np
import pandas as pd

import pandas_datareader as pdr

import matplotlib.pyplot as plt

stock_code = input("輸入代號")
start_date  = "2018-12-01"
end_date = "2019-01-05"
stock_info = pdr.data.get_data_yahoo(stock_code,start_date,end_date)
#stock_info = pdr.DataReader(stock_code, 'yahoo', start=start_date,end=end_date)
filename = stock_code+"_"+start_date+"_"+end_date
#print(filename)
print(stock_info.head())

stock_info.to_excel("%s.xlsx"%filename)
stock_info.to_csv("%s.csv"%filename)

plt.plot(stock_info["Close"],"g")
plt.savefig("%s.png"%filename)
plt.show()