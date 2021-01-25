import numpy as np
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
# 上 3 列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文 55 分、數學 60 分、國文 65 分，運用上列數據回答下列問題。
# 有多少學生英文成績比數學成績高？ #第二位、第三位、第六位同學
# 是否全班同學最高分都是國文？ #是

great = np.greater(english_score, math_score)
print(great) #[False  True  True False False  True]

highest_great_1 = np.greater(chinese_score, math_score)
print(highest_great_1) #[ True  True  True  True  True  True]
#國文成績全部高於數學成績

highest_great_2 = np.greater(chinese_score, english_score)
print(highest_great_2) #[ True  True  True  True  True  True]
#國文成績全部高於英文成績