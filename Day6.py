import numpy as np
# 1. 將下兩列 array 存成 npz 檔 
array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open('Day6.npz', 'wb') as f:
    np.savez(f, array1, array2)

# 2. 讀取剛剛的 npz 檔，加入下列 array 一起存成新的npz檔
npzfile = np.load('Day6.npz')
print(type(npzfile))
print(npzfile.files)