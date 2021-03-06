# 題目 : 將資料夾中 boston.csv 讀進來，並用圖表分析欄位。

# 畫出箱型圖，並判斷哪個欄位的中位數在 300~400 之間？

import pandas as pd
import numpy as np

x = pd.read_csv('boston(1).csv')
print(x.boxplot(figsize=(10,8)))

#欄位B

# 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？

print(x.plot.scatter(x='NOX', y='DIS'))

#成反比關係
