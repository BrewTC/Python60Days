import numpy as np
#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
a_r = array1.reshape((5,6),order='f')
print(a_r)
# [[ 0  5 10 15 20 25]
#  [ 1  6 11 16 21 26]
#  [ 2  7 12 17 22 27]
#  [ 3  8 13 18 23 28]
#  [ 4  9 14 19 24 29]]

#2.呈上題的array，找出被6除餘1的數的索引
y = array1 % 6
re_y=y.reshape((5,6),order='f')
print(re_y)
# [[0 5 4 3 2 1]
#  [1 0 5 4 3 2]
#  [2 1 0 5 4 3]
#  [3 2 1 0 5 4]
#  [4 3 2 1 0 5]]
# 列出索引值
#[0,5],[1,0],[2,1],[3,2],[4,3]

print(np.where(re_y%6==1))
# array([0, 1, 2, 3, 4], dtype=int64), array([5, 0, 1, 2, 3], dtype=int64)
