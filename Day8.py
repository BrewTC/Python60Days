import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

# 將上列 list 依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入 array
# ，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
# 呈上題，將 array 中體重(weight)數據集取出算出全部平均體重
# # 呈上題，進一步算出男生(sex 欄位是 boy)平均體重、女生(sex 欄位是 girl)平均體重



# new = np.array([('names','小明','小華','小菁','小美','小張','John','Mark','Tom'),
#                    ('sex','boy','boy','girl','girl','boy','boy','boy','boy'),
#                    ('weight',67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7),
#                    ('rank',8,1,5,4,7,6,2,3),
#                    ('myopia',True,True,False,False,True,True,False,False)],
#                    dtype=[('names','U8'),('sex','U8'),('weight','float'),('rank','int'),('myopia','?')]
#               )
