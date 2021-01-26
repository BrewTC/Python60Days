import numpy as np
array1 = np.array([[10, 8], [3, 5]])

# 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
inv_array1 = np.linalg.inv(array1)
print(inv_array1)
# [[ 0.19230769 -0.30769231]
#  [-0.11538462  0.38461538]]
matmul_array1 = np.matmul(inv_array1, array1)
print(matmul_array1)
# [[1. 0.]
#  [0. 1.]]

# 運用上列array計算特徵值、特徵向量?
eig_array1 = np.linalg.eig(array1)
print(eig_array1)
# (array([13.,  2.]), array([[ 0.93632918, -0.70710678],
#        [ 0.35112344,  0.70710678]]))

# 運用上列array計算SVD?
u, s, vh = np.linalg.svd(array1)
print(u)
# [[-0.91663818 -0.39971796]
#  [-0.39971796  0.91663818]]
print(s)
# [13.94721714  1.86417116]
print(vh)
# [[-0.74319741 -0.6690722 ]
#  [-0.6690722   0.74319741]]