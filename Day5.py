import numpy as np
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])
# 上 3 列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文 55 分、數學 60 分、國文 65 分，今天第五位同學因某原因沒來考試，導致數學成績缺值，運用上列數據回答下列問題。
# 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略？
# 第五位同學補考數學後成績為 55，請計算補考後數學成績平均、最大值、最小值、標準差？
# 用補考後資料找出與國文成績相關係數最高的學科？
english_mean = np.mean(english_score)
english_max = np.max(english_score, axis=None, out=None, keepdims=False)
english_min = np.min(english_score, axis=None, out=None, keepdims=False)
english_std = np.std(english_score)
print("五位同學英文成績平均、最大值、最小值、標準差:" , english_mean, english_max, english_min, english_std)

math_score_mean = np.nanmean(math_score)
math_score_max = np.nanmax(math_score)
math_score_min = np.nanmin(math_score)
math_score_std = np.nanstd(math_score)
print("五位同學數學成績平均、最大值、最小值、標準差:" , math_score_mean, math_score_max, math_score_min, math_score_std)

chinese_score_mean = np.mean(chinese_score)
chinese_score_max = np.max(chinese_score)
chinese_score_min = np.min(chinese_score)
chinese_score_std = np.std(chinese_score)
print("五位同學國文成績平均、最大值、最小值、標準差:" , chinese_score_mean, chinese_score_max, chinese_score_min, chinese_score_std)

new_math_score = np.array([60,85,60,68,55,60])
new_math_score_mean = np.mean(new_math_score)
new_math_score_max = np.max(new_math_score)
new_math_score_min = np.min(new_math_score)
new_math_score_std = np.std(new_math_score)
print("第五位同學補考後五位同學數學成績平均、最大值、最小值、標準差:" , new_math_score_mean, new_math_score_max, new_math_score_min, new_math_score_std)
