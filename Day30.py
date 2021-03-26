import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics

'''
# 離散均勻分配 (Discrete Uniform Distribution)
# 前提：其中有限個數值擁有相同的機率。
'''
# 1.定義離散均勻分配的基本資訊

low=1 
high=7
r = np.arange(low,high)
# 2.計算離散均勻分配的概率質量分佈 (probability mass function)
# 之所以稱為質量，是因為離散的點
# 產生 x 軸的點
#r = np.arange(stats.randint.ppf(0.01, low, high),
#        stats.randint.ppf(0.99, low, high),1)
# print(r)
# P(X=x) --> 是機率
probs = stats.randint.pmf(r,low,high)
print(probs)
plt.bar(r, probs)
plt.ylabel('P(X=x)')
plt.xlabel('x')
plt.title('pmf of DU(1,6)')
plt.show()

# 3.計算離散均勻分配的累積機率 (cumulative density function)，pmf 的累加
# P(X=x) --> 是機率
cumsum_probs = stats.randint.cdf(r, low,high)
plt.ylabel('P(X<=x)')
plt.xlabel('x')
plt.title(' cdf of DU(1,6)')
plt.plot(r, cumsum_probs)
plt.show()

# 4.透過 cdf ，給定一個 機率值，反推出對應到的 x
k = stats.randint.ppf(cumsum_probs , low, high)
print(k)
#看上圖看結果

# 5.產生符合隨機樣本點 (random sample)
X = stats.randint.rvs(low,high,size=20)
print(X)
plt.hist(X,bins=13)
plt.show()
#試試看，，每一次的結果一樣嗎?

#6.計算固定參數下，隨機變數的平均數、變異數、偏度和峰度。
stat_randint=stats.randint.stats(low,high,moments='mvks')
print(stat_randint)
print(type(stat_randint))
# 平均數
print("randint mean=",float(stat_randint[0]))
# 變異數
print("randint variance=",float(stat_randint[1]))
# 偏度
print("randint kurtosis=",float(stat_randint[2]))
# 峰度
print("randint skew=",float(stat_randint[3]))

'''
# 伯努利分配( Bernoulli Distribution )
# 前提：是只有兩種可能結果（成功或失敗）的單次隨機試驗，成功的機率為p
'''
# ①定義伯努利分配的基本資訊

# ①定義伯努利分配基本資訊
p = 0.4 # 事件A 機率 0.4
r = np.arange(0,2) # 可以出現的範圍為 0、1, 2種可能出現的結果

# ②計算二項分佈的概率質量分佈 (probability mass function)
# 之所以稱為質量，是因為離散的點
# P(X=x) --> 是機率
probs = stats.bernoulli.pmf(r,p)
#array([ 0.07776, 0.2592 , 0.3456 , 0.2304 , 0.0768 , 0.01024])
plt.bar(r, probs)
plt.ylabel('P(X=x)')
plt.xlabel('x')
plt.title('Bernoulli(p=0.4)')
plt.show()

# ③計算伯努利分配的累積機率 (cumulative density function)，pmf 的累加
# P(X=x) --> 是機率
cumsum_probs = stats.bernoulli.cdf(r,p)
plt.ylabel('P(X<=x)')
plt.xlabel('x')
plt.title('bernoulli(p=0.4)')
plt.plot(r, cumsum_probs)
plt.show()

# ④ 透過 cdf ，給定一個 機率值，反推出對應到的 x
p_loc = stats.bernoulli.ppf(cumsum_probs, p)
print(p_loc)
#看上圖看結果

# ⑤產生符合伯努利分配的隨機樣本點 (random sample)
X = stats.bernoulli.rvs(p,size=20)
print(X)
plt.hist(X)
plt.show()
#試試看，每一次的結果一樣嗎?

#6.計算固定參數下，隨機變數的平均數、變異數、偏度和峰度。
stat_ber=stats.bernoulli.stats(p,moments='mvks')
print(stat_ber)
print(type(stat_ber))
#E(X)
# 平均數
print("bernoulli mean=",float(stat_ber[0]))
# 變異數
print("bernoulli variance=",float(stat_ber[1]))
# 偏度
print("bernoulli kurtosis=",float(stat_ber[2]))
# 峰度
print("bernoulli skew=",float(stat_ber[3]))

'''
# 二項分佈 (binomial distribution)
# 前提：獨立重複試驗、有放回、只有兩個結果
# 二項分佈指出，隨機一次試驗出現事件A的機率如果為p，那麼在重複 n 次試驗中出現 x 次事件A的機率為：
# f(n,x,p) = choose(n, x) * p**x * (1-p)**(n-x)
'''
# 1.定義二項分佈的基本資訊
p = 0.5 # 事件A 機率 0.4
n = 5  # 重複實驗5次,
r = np.arange(0,6) # 可以出現的範圍為 0,1,2,...,5-->6種可能出現的結果
#print(type(k))

# 2.計算二項分佈的概率質量分佈 (probability mass function)
# 之所以稱為質量，是因為離散的點
# P(X=x) --> 是機率
probs = stats.binom.pmf(r, n, p)
#array([ 0.07776, 0.2592 , 0.3456 , 0.2304 , 0.0768 , 0.01024])
plt.bar(r, probs)
plt.ylabel('P(X=x)')
plt.xlabel('x')
plt.title('binomial(n=5,p=0.5)')
plt.show()

#學生額外小練習: 可以調整 p 的不同值，p接近於1 時，p=0.5, p 接近於 0時，看 pmf 的變化。

# 3.計算二項分佈的累積機率 (cumulative density function)，pmf 的累加
# 之所以稱為質量，是因為離散的點，預設體積（即寬度）為1
# P(X=x) --> 是機率
cumsum_probs = stats.binom.cdf(r, n, p)
#array([ 0.07776, 0.2592 , 0.3456 , 0.2304 , 0.0768 , 0.01024])
plt.show()
plt.ylabel('P(X<=x)')
plt.xlabel('x')
plt.title('binomial(n=5,p=0.4)')
plt.plot(r, cumsum_probs)
plt.show()

# 4.透過 cdf ，給定一個 機率值，反推出對應到的 x
p_loc= stats.binom.ppf(cumsum_probs, n, p)
print(p_loc)
#看上圖看結果

# 5.產生符合二項分佈的隨機樣本點 (random sample)
X = stats.binom.rvs(n,p,size=20)
#array([2, 3, 1, 2, 2, 2, 1, 2, 2, 3, 3, 0, 1, 1, 1, 2, 3, 4, 0, 3])
print(X)
plt.hist(X)
plt.show()
#試試看，，每一次的結果一樣嗎?

#6.計算固定參數下，隨機變數的平均數、變異數、偏度和峰度。
stat_bin=stats.binom.stats(n,p,moments='mvks')
print(stat_bin)
print(type(stat_bin))
#E(X)
print("binomial mean=",float(stat_bin[0]))
print("binomial variance=",float(stat_bin[1]))
print("binomial kurtosis=",float(stat_bin[2]))
print("binomial skew=",float(stat_bin[3]))

# 機率可以怎麼用？
# 丟一個銅板，丟了100次，出現正面 50 次的機率有多大。
# (提示：先想是哪一種分配，然後透過 python 語法進行計算)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
# 這是 貝努利(bermoulli)分配
p = 0.5 # 假設是公平硬幣
n = 100  # 重複實驗 100次,
r = 50 # 計算出現50次正面


# 2.計算二項分佈的概率質量分佈 (probability mass function)
# 之所以稱為質量，是因為離散的點
# P(X=x) --> 是機率
probs = stats.binom.pmf(r, n, p)
print(probs)
