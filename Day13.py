# 對以下成績資料做分析:
import pandas as pd

score_df = pd.DataFrame([[1,56,66,70], [2,90,45,34], [3,45,32,55], [4,70,77,89], [5,56,80,70], [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]], columns=['student_id','math_score','english_score','chinese_score'])
student_id_score_df = score_df.set_index('student_id')
print(student_id_score_df)

# 6 號學生(student_id=6) 3 科平均分數為何
student_id_score_df = student_id_score_df.mean(axis=1)
print(student_id_score_df.loc[6])
#56.333333333333336

# 6 號學生 3 科平均分數是否有贏過班上一半的同學？
print(student_id_score_df.median())
#59.833333333333336
#56.33 < 59.83 ,沒有贏過班上一半的學生

# 由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？
new_student_id_score_df = student_id_score_df.apply(lambda x : x**(0.5)*10)
print(new_student_id_score_df.loc[6])
# math_score       77.459667
# english_score    73.484692
# chinese_score    74.161985

# 承上題，加分後各科班平均變多少？
print(new_student_id_score_df.mean(axis=0))
# math_score       74.194221
# english_score    78.350301
# chinese_score    78.739928
