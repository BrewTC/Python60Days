import numpy as np
# 1. 將下兩列 array 存成 npz 檔 
array1 = np.array(range(30))
array2 = np.array([2,3,5])
np.savez('Day6.npz', array1, array2)

# 2. 讀取剛剛的 npz 檔，加入下列 array 一起存成新的npz檔
load_array = np.load('Day6.npz')
array3 = np.array([[4,5,6],[1,2,3]])
np.savez('new_array.npz', load_array['arr_0'], load_array['arr_1'], array3)
