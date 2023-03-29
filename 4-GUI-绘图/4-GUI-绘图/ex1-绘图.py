# encoding = utf-8
import  cv2
import numpy as np
import cv2
import numpy as np
# 1.初始化全0图像
img = np.zeros((640, 480, 3))

# 2.绘制直线
#  参数设置：图像、端点1坐标、端点2坐标、颜色元组，线条粗细
cv2.line(img, (0, 0), (249, 249), (0, 255, 0), 2)

# 3.绘制矩形
#  参数设置：图像、左上角坐标、右下角坐标、颜色元组，线条粗细
cv2.rectangle(img, (0, 0), (249, 249), (255, 255, 255), 3)
# 4.绘制圆
#  参数设置：图像、圆心坐标、半径、颜色元组，线条粗细
cv2.circle(img, (300, 300), 50, (0, 255, 0), 3)

# 5. 显示文字
#  参数设置：图像、文本内容、起始坐标、字体格式、字体大小、颜色元组，线条粗细
cv2.putText(img,'woshiCVer', (150,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
cv2.imshow('win',img)
# 画面刷新
cv2.waitKey(0)

