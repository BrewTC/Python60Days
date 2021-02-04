# 題目：運下列時間序列資料做運算
import pandas as pd
import numpy as np

index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)
# print(index, series)

# 將所有轉為周資料
q1 = index.to_period('W')
print(q1) 
# 2018-12-31/2019-01-06     0
# 2018-12-31/2019-01-06     1
# 2018-12-31/2019-01-06     2
# 2018-12-31/2019-01-06     3
# 2018-12-31/2019-01-06     4
# 2018-12-31/2019-01-06     5
# 2019-01-07/2019-01-13     6
# 2019-01-07/2019-01-13     7
# 2019-01-07/2019-01-13     8
# 2019-01-07/2019-01-13     9
# 2019-01-07/2019-01-13    10
# 2019-01-07/2019-01-13    11
# 2019-01-07/2019-01-13    12
# 2019-01-14/2019-01-20    13
# 2019-01-14/2019-01-20    14
# 2019-01-14/2019-01-20    15
# 2019-01-14/2019-01-20    16
# 2019-01-14/2019-01-20    17
# 2019-01-14/2019-01-20    18
# 2019-01-14/2019-01-20    19
# Freq: W-SUN, dtype: int64

# 將周資料的值取平均
q2 = series.resample('W').mean()
print(q2)
# 2019-01-06     2.5
# 2019-01-13     9.0
# 2019-01-20    16.0
