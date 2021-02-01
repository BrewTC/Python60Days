# 讀取資料夾中 boston.csv 讀取其欄位 CHAS、NOX、RM，輸出成 .xlsx 檔案
import pandas as pd
new_boston = pd.read_csv('boston.csv', usecols=['CHAS', 'NOX', 'RM'])
# print(new_boston)

# xlsx_boston = pd.read_excel('new_boston.csv')
# print(xlsx_boston)

# new_boston = new_boston.to_excel('new_boston.xlsx')
# print(new_boston)