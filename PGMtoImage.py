#RAWtoImage(NIR,RGB)画像に分割する用
#バイナリを開いてファイルを変換

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Rawファイルの読み込み
rawpath = "./Image/prefix_0.raw"
width=1024
height=1024
fd = open(rawpath, 'rb')
f = np.fromfile(fd, dtype=np.int16, count=height*width)
img = f.reshape((height,width))
fd.close()

# Raw.pngの作成
#plt.imshow(img, cmap="gray")
#plt.show()
cv2.imwrite("./Image/Raw.png",img)