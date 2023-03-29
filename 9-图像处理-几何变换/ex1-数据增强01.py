# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 1. 图像平移： 下、上、右、左平移
def img_translation(image):
    # 1.1 下移变换矩阵
    M = np.float32([[1, 0, 0],
                    [0, 1, 100]])
    # 1.2 对图像进行变换
    img_down = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))


    # 1.3 右移变换矩阵
    M = np.float32([[1, 0, 100],
                    [0, 1, 100]])

    # 1.4 对图像进行变换
    img_right = cv2.warpAffine(image, M ,(image.shape[1],image.shape[0]))

    # 1.9 显示图形 下移、右移
    cv2.imshow("down", img_down)


# 2.图像缩放
def img_scale(image):
    # 2.1 指定缩放图像大小
    result = cv2.resize(image, (200, 100))
    cv2.imshow("scale", result)

    # 2.2 缩放比例
    # fx：width方向的缩放比例
    # fy：height方向的缩放比例
    result2 = cv2.resize(image, None, fx=0.5, fy=2.0)
    cv2.imshow("scale2", result2)


# 3. 图像翻转
def img_flip(image):
    # 3.1 0以X轴为对称轴翻转,>0 以Y轴为对称轴翻转, <0 X轴Y轴翻转
    horizontally = cv2.flip(image, 0)  # 水平镜像
    vertically = cv2.flip(image, 1)  # 垂直镜像
    # 水平垂直镜像
    hv = cv2.flip(image, -1)

    # 3.2 显示图形

    cv2.imshow("Horizontally", horizontally)
    cv2.imshow("Vertically", vertically)
    cv2.imshow("Horizontally & Vertically", hv)

if __name__ == '__main__':
    # 0. 加载图像数据
    src = cv2.imread('butterfly.jpg')
    # 1. 图像平移
    img_translation(src)
    # 2. 图像缩放
    img_scale(src)
    # 3. 图像翻转
    img_flip(src)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
