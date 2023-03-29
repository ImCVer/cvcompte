# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 4 图像旋转
def img_rotation(image):
    # 4.1 原图的高、宽 以及通道数
    rows, cols, _ = image.shape
    # 4.2 绕图像的中心旋转
    # 参数矩阵M：旋转中心 旋转度数 缩放比例
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2),180, 1)
    # 4.3 仿射变换
    # 参数：原始图像 旋转参数 元素图像宽高
    rotate = cv2.warpAffine(image, M, (cols,rows))
    # 4.4 显示图像
    cv2.imshow("rotate",rotate)


# 5.图像加噪
def img_noise(img, nums):
    # 5.1 原图的高、宽 以及通道数
    rows, cols, chn = img.shape

    # 5.2 循环添加噪声
    for i in range(nums):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y, :] = 255

    # 5.3 显示图像
    cv2.imshow("test_noise", img)


# 添加高斯噪声
def img_noise2(image, mean=0, var=0.001):
    '''
        mean : 均值
        var : 方差
    '''
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)

    cv2.imshow("noise", out)


# 6. 图像亮度调节
def img_brightness(image):

    # 6.1 参数设置
    contrast = 1  # 对比度
    brightness = -200  # 亮度
    # 6.2 图像融合
    pic_turn = cv2.addWeighted(image, contrast, image, 0, brightness)
    # cv2.addWeighted(对象,对比度,对象,对比度)
    '''cv2.addWeighted()实现的是图像透明度的改变与图像的叠加'''
    # 6.3 显示图像
    cv2.imshow('bright', pic_turn)  # 显示图片



if __name__ == '__main__':

    # 0. 加载图像数据
    src = cv2.imread('butterfly.jpg')

    # 4. 图像旋转
    img_rotation(src)
    # 5. 添加噪声
    img_noise(src, 3000)
    # 6. 增加亮度
    img_brightness(src)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
