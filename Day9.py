# 讀取資料夾中 boston.csv 讀取其欄位 CHAS、NOX、RM，輸出成 .xlsx 檔案
import pandas as pd
new_boston = pd.read_csv('boston.csv', usecols=['CHAS', 'NOX', 'RM'])
# print(new_boston)

new_boston.to_excel('hw_boston.xlsx')
# pip install xlwt-future
# pip  install openpyxl
# 有的py不相容存取xlsx檔，還沒解決此問題
