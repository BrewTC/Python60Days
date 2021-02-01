#將以下問卷資料的職業(Profession) 欄位缺失值填入字串 'others'，更進一步將字串做編碼。 此時用什麼方式做編碼比較適合？為什麼？
import pandas as pd 

q_df = pd.DataFrame([['male', 'teacher'], 
                     ['male', 'engineer'],
                     ['female', None], 
                     ['female', 'engineer']]
                     ,columns=['Sex','Profession'])

new_q_df = q_df.fillna('others')
# print(new_q_df)

pf = pd.q_df.get_dummies(q_df['Profession'])
df = pd.concat([q_df,pf], axis=1)
print(df)

#用一般型的排序方式，因為職業類別是沒有順序的編碼