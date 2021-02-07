# 1.畫出 cos 圖檔，並儲存
# 載入需要的...
import matplotlib.pyplot as plt
import numpy as np

# 準備數據 ... 假設我要畫一個sin波 從0~180度
# 設定要畫的的x,y數據list....
# 載入需要的...
import matplotlib.pyplot as plt
import numpy as np

# 準備數據 ... 假設我要畫一個sin波 從0~180度
# 設定要畫的的x,y數據list....
x = np.arange(0,180)
y = np.cos(x * np.pi / 180.0)

# 開始畫圖
plt.plot(x,y)
# 在這個指令之前，都還在做畫圖的動作 
# 這個指令算是 "秀圖"
plt.show() 

#畫出完整的 sin 圖形
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)

plt.plot(x, y_sin)

plt.show()

#畫出完整的 cos 圖形
x = np.arange(0, 3 * np.pi, 0.1)
y_cos = np.cos(x)

plt.plot(x, y_cos)

plt.show()


# 2.給定散點圖顏色
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

T = np.arctan2(Y,X)
plt.scatter(X,Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

plt.show()
