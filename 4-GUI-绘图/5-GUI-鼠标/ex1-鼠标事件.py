# encoding = utf-8
import  cv2
import numpy as np

# 5.定义回调函数
def callback(event,x , y, flags, param):
    pass
    # 5.1 打印输出event,x,y,flags
    # cv2.line(img, (x, y), 15, (0, 255, 0), 2)
    print(event, x, y, flags)
    #  5.2 如果鼠标触发双击事件，绘制一个蓝色实心圆圈
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.line(img, (x, y), 15, (0, 255, 0), -1)
         cv2.circle(img, (x, y), 15, (255, 0, 0), -1)

    # 5.3 判断是否发生滚轮事件与CTRL按键同时发生
    if event == cv2.EVENT_MOUSEWHEEL and (flags & cv2.EVENT_FLAG_CTRLKEY):
        # 5.4 判断flags变量，滚轮向上，打印“up”；滚轮向下，打印“down”
        if flags > 0:
            print('up')
        else:
            print('down')


# 1. 加载考拉图像
img = cv2.imread('Koala.jpg')

# 2. 定义图像显示窗口
cv2.namedWindow('chuangkou')

# 3.设置鼠标回调事件-函数
cv2.setMouseCallback('chuangkou', callback)

# 4循环控制
while True:
    # 4.1显示图像
    cv2.imshow('chuangkou', img)
    # 4.2 刷新图像
    key = cv2.waitKey(33)
    # 4.3 键盘输入q，跳出循环
    if key == ord('q'):
        break








