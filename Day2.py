import numpy as np
#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
a_r = array1.reshape((5,6),order='f')
print(a_r)
#2.呈上題的array，找出被6除餘1的數的索引
y = array1 % 6
re_y=y.reshape((5,6),order='f')
print(re_y)