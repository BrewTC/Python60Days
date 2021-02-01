# 讀取 STOCK_DAY_0050_202009.csv 串聯 STOCK_DAY_0050_202010.csv，並且找出 open 小於 close 的資料
import pandas as pd

#讀取兩個csv檔案
stock1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
stock2 = pd.read_csv('STOCK_DAY_0050_202010.csv')
# print(stock1)
# print(stock2)

#串聯起來
stock_data = pd.concat([stock1,stock2])
# print(stock_data)

#找出open小於close的資料
stock_data2 = stock_data[stock_data.open < stock_data.close]
# print(stock_data2)
