import numpy as np
import seaborn as sns

#設定圖形樣式 - whitegrid
# use sns.set
sns.set(style="whitegrid")

# 利用 NUMPY 去建立資料集
# np.random.RandomState 設定數學式
'''
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)
'''
rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

# 畫圖
# sns.residplot

sns.residplot(x, y, lowess=True, color="g")

# 繪製單變數分佈:快速檢視海出生單變數分佈的最便捷方式是distplot() 函數。
# 默認情況下,這將繪製直方圖並適合內核密度估計值(KDE)。


# 2.1使用distplot()使用簡單的規則來正確猜測預設情況下正確的數位,但嘗試更多或更少的 bin 可能會顯示資料中的其他特徵: 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
sns.set(color_codes=True)

# bin: 指的是特徵值, 
# kde: on/off
# sns.distplot();

sns.distplot(x, bins=15, kde=False, rug=True);

# 2.2有無kde對圖形分布的影響

sns.distplot(x, bins=15, kde=True, rug=True);
