import cv2
import os

# 1.图片文件夹路径
filepath = './images'

# 2.使用os模块列举所有图片
filelist = os.listdir(filepath)

# 3.输出文件列表
print(filelist)

# # 4.循环遍历文件列表
for f in filelist:

    # 4.1 拼接文件路径
    file = filepath + '/' + f
    print(file)
#     # 4.1 读取图片
#     img = cv2.imread(file)
#
#     # 4.3 显示图片
#     cv2.imshow(f, img)
#
#     # 4.4 等待按键
#     cv2.waitKey(5000)


