#RAWtoImage(NIR,RGB)画像に分割する用
#バイナリを開いてファイルを変換

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Rawファイルの読み込み
Rawlen = 1024
rawpath = "./Image/prefix_0.raw"
fd = open(rawpath, 'rb')
f = np.fromfile(fd, dtype=np.int16, count=Rawlen*Rawlen)
img = f.reshape((Rawlen,Rawlen))
fd.close()

# Raw.pngの作成
cv2.imwrite("./Image/Raw.png",img)

# NIR画像の作成
height = 512
width = 512
NIR_Image = np.zeros((height, width), np.uint8)
NIR_Image[0][0:width] = img[0][0:width]
for i in range(Rawlen):
    if i % 2 == 0:
        NIR_Image[i//2][0:width] = img[i][0:width]

# png画像と比較してできたか確認
# 同一画像化確認　Ture なら一緒
OriN = cv2.imread("./Image/NIR.png",cv2.IMREAD_GRAYSCALE) # NIR
OriR = cv2.imread("./Image/Red.png",cv2.IMREAD_GRAYSCALE) # Red
OriB = cv2.imread("./Image/Blue.png",cv2.IMREAD_GRAYSCALE) # Blue
OriG = cv2.imread("./Image/Green.png",cv2.IMREAD_GRAYSCALE) # Green
print(np.array_equal(OriN, NIR_Image))
