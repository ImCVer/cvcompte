# 1.导入opencv库
import cv2

# 2.读取图像
img = cv2.imread('./images/butterfly.jpg', cv2.IMREAD_COLOR)

# 3. 形状  (768, 1024, 3)  三通道  RGB
# 形状  (768, 1024) 单通道，灰度图
print(img.shape)





# 4. img类型
print(type(img))
# 5. 显示图像
cv2.imshow('butterfly', img)

# 6. 刷新图像，等待用户按键
cv2.waitKey(0)

