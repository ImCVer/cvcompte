import  cv2
import  numpy as np

# 1. 加载图像
img = cv2.imread('butterfly.jpg')

# 2. 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 3. 转换为HSV图像
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 4. 显示原图、GRAY、HSV图像
cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)



# 5. 使用numpy定义仅有一个像数点的图像,数据类型为无符号8位整型
ghsv = np.array([[[0, 255, 0]]], dtype=np.uint8)

# 6. 将改图像转换为HSV
ghsv = cv2.cvtColor(ghsv, cv2.COLOR_BGR2HSV)
print(ghsv)

## 7. inRange函数实现对颜色空间的提取 - 提取butterfly图片中红色部分
'''
cv2.inRange(hsv, lower_red, upper_red)
参数解析：
第一个参数：hsv指的是原图
第二个参数(ndarray)：lower_red指的是图像中低于这个lower_red的值，图像值变为0
第三个参数(ndarray)：upper_red指的是图像中高于这个upper_red的值，图像值变为0
而在lower_red～upper_red之间的值变成255
'''
lower_red = np.array([0, 43, 46])
upper_red = np.array([10, 255, 255])
res= cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow('res', res)


cv2.waitKey(0)
