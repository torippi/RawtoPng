#RAWtoImage(NIR,RGB)画像に分割する用
#バイナリを開いてファイルを変換

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Rawファイルの読み込み
FN = 7831
for i in range(1800):
    print(str(i+1) + "枚目")
    Rawlen = 1024
    rawpath = "../Rawdata/First/prefix_{}".format(i)+"_1024x1024_2B_LE_FN{}".format(FN)+"_FD0_FS0.raw"
    while os.path.exists(rawpath) == False:
        print("フレームが抜けてる")
        FN = FN + 1
        rawpath = "../Rawdata/First/prefix_{}".format(i)+"_1024x1024_2B_LE_FN{}".format(FN)+"_FD0_FS0.raw"
    fd = open(rawpath, 'rb')
    f = np.fromfile(fd, dtype=np.int16, count=Rawlen*Rawlen)
    img = f.reshape((Rawlen,Rawlen))
    fd.close()

    # Raw.pngの作成
    cv2.imwrite("../Convert/First/Raw/{:0=4}".format(i)+".png",img)

    # NIR画像の作成
    height = 512
    width = 512
    NIR_Image = np.zeros((height, width), np.uint8)
    Red_Image = np.zeros((height, width), np.uint8)
    Blue_Image = np.zeros((height, width), np.uint8)
    Green_Image = np.zeros((height, width), np.uint8)
    for q in range(Rawlen):
        if q % 2 == 0: #0,2,4,6,8,...
            NIR_Image[q//2][0:width] = img[q][np.arange(0, 1024, 2)]
            Green_Image[q//2][0:width] = img[q][np.arange(1, 1024, 2)]
        else: #1,3,5,7,9,...
            Red_Image[q//2][0:width] = img[q][np.arange(0, 1024, 2)]
            Blue_Image[q//2][0:width] = img[q][np.arange(1, 1024, 2)]

    cv2.imwrite("../Convert/First/NIR/{:0=4}".format(i)+".png",NIR_Image)
    cv2.imwrite("../Convert/First/Red/{:0=4}".format(i)+".png",Red_Image)
    cv2.imwrite("../Convert/First/Blue/{:0=4}".format(i)+".png",Blue_Image)
    cv2.imwrite("../Convert/First/Green/{:0=4}".format(i)+".png",Green_Image)
    FN = FN + 1

