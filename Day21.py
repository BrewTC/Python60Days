# 1. FacetGrid 類有助於可視化一個變數的分佈，以及使用多個面板在數據集子集中分別顯示多個變數之間的關係

# 作業：取得另一個 dataset：titanic

# 做箱形圖
# 利用 facet grid 繪圖並分析
# 繪製小提琴圖

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('titanic')

df.info()

# 直接使用PANDAS dataframe, 當作參數
#條形圖()顯示分類變數和連續變數之間的關係。數據以矩形條表示,其中條的長度表示該類別中數據的比例。

sns.barplot(data = df, x= 'sex', y='survived', hue = "class")
plt.show()

# 2. 在上面的示例中,我們可以看到每個班級中男性和女性的平均存活率。從情節中,我們可以理解,女性存活人數比男性多。在男性和女性中,更多的存活率來自頭等艙。

# barplot 中的特殊情況是顯示每個類別中的觀測值的"否",而不是計算第二個變數的統計資訊。

# 繪製數據子集的小倍數。 FacetGrid 示例,

# FacetGrid 類有助於可視化一個變數的分佈,以及使用多個面板在數據集子集中分別顯示多個變數之間的關係。

# 瞭解性別在各艙等的分布的存活率

g = sns.FacetGrid(df, col = "survived")
g.map(plt.hist,"sex")
plt.show()


#3. 先檢視各艙位存活人數，此時可以使用groupby函數進行分類，
#其中 survived＝1表示存活，survived＝0表示死亡，將survived加總即為各艙等生存人數。

df.groupby('pclass').survived.sum()

#加上性別
survived=df.groupby(['pclass','sex']).survived.sum()
survived.plot(kind='bar')

#使用pd.crosstab函數繪製交叉表，交叉表可以很直觀的依據艙位等級及性別來查看存活人數及死亡人數。
#繪製堆疊條形圖，x軸代表依據艙等分成男性及女性，y軸代表人數，其中藍色代表死亡人數，橘色代表存活人數。
survived_counts = pd.crosstab([df.pclass, df.sex],df.survived)
survived_counts 

survived_counts.plot(kind='bar', stacked=True)


# 直接使用PANDAS dataframe, 當作參數
#條形圖()顯示分類變數和連續變數之間的關係。數據以矩形條表示,其中條的長度表示該類別中數據的比例。

sns.violinplot(data=survived_counts)
plt.show()


# 瞭解性別在各艙等的分布的存活率
g = sns.FacetGrid(df, col = "survived")
g.map(plt.hist,"pclass")
plt.show()

h = sns.FacetGrid(df, col = "survived")
h.map(plt.hist,"sex")
plt.show()
# PS: 跟第一次做 Face.Grid 有何不同??
