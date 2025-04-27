import cv2
import numpy as np

# 读取图片
image = cv2.imread("\图片\测试图片\t11.png", cv2.IMREAD_GRAYSCALE)

# 应用二值化，将文字和背景分开
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# 找到轮廓
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 初始化一个空的列表来保存分割后的字符
characters = []

# 遍历找到的轮廓
for contour in contours:
    # 获取轮廓的边界框
    x, y, w, h = cv2.boundingRect(contour)

    # 如果字符太小或太大，则忽略它
    if 10 < w < 100 and 10 < h < 100:
        # 从原图中裁剪出字符
        char_img = image[y:y + h, x:x + w]

        # 缩放字符到统一大小，便于后续处理
        char_img_resized = cv2.resize(char_img, (32, 32))

        # 将裁剪并缩放后的字符添加到列表中
        characters.append(char_img_resized)

# 显示分割后的字符
for i, char in enumerate(characters):
    cv2.imshow(f'Character {i}', char)

cv2.waitKey(0)
cv2.destroyAllWindows()