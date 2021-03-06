# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns

# 輸入資料
boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170,
 164, 173, 165, 163, 177, 171]

# 計算統計量_平均數的方法
mean_boy=np.mean(boys)
print("男孩身高平均=",mean_boy)

statistics_mean_boy=statistics.mean(boys)
print("statistics_mean_boy=",statistics_mean_boy)

# 計算統計量_中位數的方法
np_median_boy=np.median(boys,axis=None)
print("np_median_boy=",np_median_boy)

statistics_median_boy=statistics.median(boys)
print("statistics_median_boy=",statistics_median_boy)

# 統計量_眾數
# 統計量的眾數，如果有多個眾數，取最小的值當眾數。
mode_boy=stats.mode(boys,axis=None)
print("男孩身高眾數=",mode_boy)
print("男孩身高眾數=",mode_boy[0][0])


# 統計量_眾數
statistics_mode_boy=statistics.mode(boys)
print("statistics_mode_boy=",statistics_mode_boy)

#全距
#rangeV=max(boys)-min(boys)
def rangeV(x): 
  return(max(x)-min(x))
    
print(rangeV(boys))

# 計算變異數的方法
print("男孩身高變異數=",statistics.variance(boys))
print("男孩身高變異數=",np.var(boys,ddof=1))

# 統計量_標準差的方法
# 樣本標準差
#ddof=1, 回傳 sample standard deviation 樣本標準差，分母(n-1)，無偏估計
std_boy=np.std(boys,ddof=1)
print("男孩身高標準差=",std_boy)

statistics_stdev_boy=statistics.stdev(boys)
print("statistics_mean_boy=",statistics_stdev_boy)

# python 百分位數
# np
print("90百分位數=",np.percentile(boys, 90))
print("50百分位數=",np.percentile(boys, 50))
print("20百分位數=",np.percentile(boys, 20))
#stat
print("20百分位數=",stats.scoreatpercentile(boys, 20))

#計算峰度和偏度
print(stats.skew(boys))
print(stats.kurtosis(boys))

# pandas和 stat 接近
# python的峰帶

#最後，畫圖看分布
plt.hist(boys,alpha=.4,bins=40)
plt.title('boy,skewness={0},kurtosis={1}'.format(round(stats.skew(boys),2),round(stats.kurtosis(boys),2)))
plt.axvline(x=mean_boy)
plt.show()

# 今天學到不同統計量之間特性，
# 試著分析男生女生身高資料，
# 試著回答下面的問題:
# Q1:試著用今天所教的內容，如何描述這兩組資料的樣態?
# 計算統計量_平均數的方法
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns

boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170,
 164, 173, 165, 163, 177, 171]

girls=[169, 183, 170, 168, 182, 170, 173, 185, 151, 156, 162, 169, 162, 181,
 159, 154, 167, 175, 170, 160]

mean_boy=np.mean(boys)
print("男孩身高平均=",mean_boy)
mean_girl=np.mean(girls)
print("女孩身高平均=",mean_girl)

# 計算統計量_中位數的方法
np_median_boy=np.median(boys,axis=None)
print("男孩身高中位數=",np_median_boy)
np_median_girl=np.median(girls,axis=None)
print("女孩身高中位數=",np_median_girl)

#計算統計量_眾數
mode_boy=stats.mode(boys,axis=None)
print("男孩身高眾數=",mode_boy[0][0])

mode_girl=stats.mode(girls,axis=None)
print("女孩身高眾數=",mode_girl[0][0])

#計算全距:
def rangeV(x): 
  return(max(x)-min(x))
    
print("男孩身高全距=",rangeV(boys))
print("女孩身高全距=",rangeV(girls))

#計算變異數
print("男孩身高變異數=",np.var(boys,ddof=1))
print("男孩身高變異數=",np.var(girls,ddof=1))


#計算標準差
std_boy=np.std(boys,ddof=1)
print("男孩身高標準差=",std_boy)
std_girl=np.std(girls,ddof=1)
print("女孩身高標準差=",std_girl)

## python 百分位數
#np
print("男孩身高90百分位數=",np.percentile(boys, 90))
print("男孩身高50百分位數=",np.percentile(boys, 50))
print("男孩身高20百分位數=",np.percentile(boys, 20))

print("女孩身高90百分位數=",np.percentile(girls, 90))
print("女孩身高50百分位數=",np.percentile(girls, 50))
print("女孩身高20百分位數=",np.percentile(girls, 20))


#計算峰度和偏度
print("男孩身高偏度=",stats.skew(boys))
print("男孩身高峰度=",stats.kurtosis(boys))

print("女孩身高偏度=",stats.skew(girls))
print("女孩身高峰度=",stats.kurtosis(girls))

#最後，畫圖看分布，boys
plt.hist(boys,alpha=.4,bins=40)
plt.title('boy,skewness={0},kurtosis={1}'.format(round(stats.skew(boys),2),round(stats.kurtosis(boys),2)))
plt.axvline(x=mean_boy)
plt.show()

#最後，畫圖看分布,girls
plt.hist(girls,alpha=.4,bins=40,color=sns.desaturate("indianred", .8))
plt.title('girl,skewness={0},kurtosis={1}'.format(round(stats.skew(girls),2),round(stats.kurtosis(girls),2)))
plt.axvline(x=mean_girl,color=sns.desaturate("indianred", .8))
plt.show()

plt.hist(boys,alpha=.4)
plt.hist(girls,color=sns.desaturate("indianred", .8),alpha=.4)
plt.title("all samples")
plt.axvline(x=mean_girl,color=sns.desaturate("indianred", .8))
plt.axvline(x=mean_boy)
plt.show()

# Q2: 請問男生和女生在平均身高上誰比較高?
# 計算統計量_平均數的方法
mean_boy=np.mean(boys)
print("男孩身高平均=",mean_boy)
mean_girl=np.mean(girls)
print("女孩身高平均=",mean_girl)
# 女生平均而言比較高
# 從分布看的出來，女生的平均身高較高，且資料較為集中，男生的資料較為分散

# Q3:請問第二題的答案和日常生活中觀察的一致嗎? 如果不一致，你覺得原因可能為何?
# 答案如下: 和日常的觀察不一致，
# 有可能是抽樣上有誤差，此樣本和母體的特性差異比較大。
