#encoding = utf-8

import  cv2
import  numpy as np

# 6 定义全局变量:
lbtndown = False  # 记录鼠标左键状态
tx, ty = 0, 0  # 记录ROI区域左上角坐标
bx, by = 0,0  # 记录ROI区域右下角坐标


#  7.定义一个鼠标回调函数
def callback(event, x, y, flags, param):
    # 7.1  引用全局变量
    global tx,ty,by,bx,lbtndown
    # 7.2 判断event是否为左键按下， 记录左上角坐标值,变更鼠标左键状态为True
    if event == cv2.EVENT_LBUTTONDOWN:
        tx, ty = x, y
        lbtndown = True
    # 7.3 判断是否为鼠标滑动
    elif event == cv2.EVENT_MOUSEMOVE:
        # 若戍边左键是按下状态，则记录右下角坐标值，在img2中绘制矩形框
        if lbtndown == True:
            by, bx = y , x
            img2 = img.copy()
            cv2.rectangle(img2, (tx, ty), (bx, by), (255,0, 0), 2)
            cv2.imshow('chuangkou', img2)
    # 7.4 是否为鼠标释放， 记录右下角坐标值，绘制矩形框（最终选中）,更改lbtndown状态
    elif event == cv2.EVENT_LBUTTONUP:
        bx, by = x, y
        cv2.rectangle(img, (tx,ty),(bx,by), (0,255,0),2)
        lbtndown = False

# 1 加载图像
img = cv2.imread("Koala.jpg")

# 2 调整图像大小-缩放(640,480)
img = cv2.resize(img,(640, 480))
# 3 定义显示图像窗口
cv2.namedWindow('chuangkou')
# 4 设置鼠标回调事件
cv2.setMouseCallback('chuangkou',callback)
# 5 循环刷新图像
while True:
    cv2.imshow("chuangkou", img)
    key = cv2.waitKey(33)
    if key == ord(' '):
        break

