# RAWtoImage(NIR,RGB)画像に分割する用
# たくさんのファイルを一括
# バイナリを開いてファイルを変換

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Rawフォルダの読み込み
# Rawファイルの読み込み
Rawlen = 1024
rawpath = "../Rawdata/First/prefix_0_1024x1024_2B_LE_FN7831_FD0_FS0.raw"
fd = open(rawpath, 'rb')
f = np.fromfile(fd, dtype=np.int16, count=Rawlen*Rawlen)
img = f.reshape((Rawlen,Rawlen))
fd.close()

# Raw.pngの作成
cv2.imwrite("../Convert/First/Raw/0001.png",img)

# NIR画像の作成
height = 512
width = 512
NIR_Image = np.zeros((height, width), np.uint8)
Red_Image = np.zeros((height, width), np.uint8)
Blue_Image = np.zeros((height, width), np.uint8)
Green_Image = np.zeros((height, width), np.uint8)
NIR_Image[0][0:width] = img[0][0:width]
for i in range(Rawlen):
    if i % 2 == 0:
        NIR_Image[i//2][0:width] = img[i][0:width]
        Green_Image[i//2][0:width] = img[i][512:1024]
    else:
        Red_Image[i//2][0:width] = img[i][0:width]
        Blue_Image[i//2][0:width] = img[i][512:1024]

cv2.imwrite("../Convert/First/NIR/0001.png",NIR_Image)
cv2.imwrite("../Convert/First/Red/0001.png",Red_Image)
cv2.imwrite("../Convert/First/Blue/0001.png",Blue_Image)
cv2.imwrite("../Convert/First/Green/0001.png",Green_Image)