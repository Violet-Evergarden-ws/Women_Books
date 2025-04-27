from PIL import Image
import numpy as np


def split_image(picture_path):
    pic_org = Image.open(picture_path)  # 读取路径图片信息
    pic_org = pic_org.convert('L')
    pic_org = pic_org.resize((650, 650))
    pic_org = np.asarray(pic_org).copy()
    (r, l) = pic_org.shape
    for i in range(r):
        if sum(1 for x in pic_org[i] if x <= 150) / l >= 0.7:
            pic_org[i] = 255
    for j in range(l):
        l_small = 0
        l_big = 0
        for pic_org1 in pic_org:
            if pic_org1[j] <= 150:
                l_small += 1
        if l_small / r >= 0.7:
            for i in range(r):
                pic_org[i][j] = 255
    pic = pic_org
    (r, l) = pic.shape
    row1 = []
    row2 = []
    # 确定row1,row2用于分割图片
    for i in range(r):
        if i == 0:
            if np.min(pic[i]) <= 30 and np.min(pic[i + 1]) <= 30:
                row1.append(0)
                continue
        else:
            if np.min(pic[i - 1]) > 30 >= np.min(pic[i]) and i != r - 1:
                row1.append(i)
                continue
        if i == r - 1:
            if np.min(pic[i - 1]) <= 30 < np.min(pic[i]):
                row2.append(r - 1)
                continue
            if len(row1) > len(row2):
                row2.append(r - 1)
        else:
            if np.min(pic[i - 1]) <= 30 < np.min(pic[i]) and i - 1 > 0 and i != 0:
                row2.append(i)
                continue
    row_D = np.asarray(row2) - np.asarray(row1)
    row_1 = []
    row_2 = []
    for i in range(len(row1)):
        if row2[i] - row1[i] < np.max(row_D) / 3:
            if i == 0:
                row1[i + 1] = row1[i]
                continue
            elif i == len(row1) - 1:
                row_2[-1] = row2[i]
                continue
            elif not row_2:
                row1[i + 1] = row1[i]
                continue
            else:
                if row1[i] - row_2[-1] >= row1[i + 1] - row2[i]:
                    row1[i + 1] = row1[i]
                    continue
                elif row1[i] - row_2[-1] < row1[i + 1] - row2[i]:
                    row_2[-1] = row2[i]
                    row1[i] = row_1[-1]
                    continue
        else:
            row_1.append(row1[i])
            row_2.append(row2[i])

    pic2 = []
    for i in range(len(row_1)):
        pic2.append(pic[row_1[i]:row_2[i], :])
    line1 = []
    line2 = []
    for k in range(len(pic2)):
        pic3 = pic2[k]
        line_1 = []
        line_2 = []
        for j in range(l):
            if j == 0:
                if np.min(pic3[:, j]) <= 30 and np.min(pic3[:, j + 1]) <= 30:
                    line_1.append(0)
                    continue
            else:
                if np.min(pic3[:, j - 1]) > 30 >= np.min(pic3[:, j]) and j != l - 1:
                    line_1.append(j)
                    continue
            if j == l - 1:
                if np.min(pic3[:, j - 1]) <= 30 < np.min(pic3[:, j]):
                    line_2.append(l - 1)
                    continue
                elif len(line_1) > len(line_2):
                    line_2.append(l - 1)
                    continue
            else:
                if np.min(pic3[:, j - 1]) <= 30 < np.min(pic3[:, j]) and j - 1 > 0 and j != 0:
                    line_2.append(j)
                    continue
        line1.append(line_1)
        line2.append(line_2)
    line_1 = []
    line_2 = []
    for i in range(len(line1)):
        lines_1 = []
        lines_2 = []
        line_D = np.asarray(line2[i]) - np.asarray(line1[i])
        for j in range(len(line1[i])):
            # 这里要改
            if line2[i][j] - line1[i][j] < np.max(line_D) / 3:
                if j == 0:
                    line1[i][j + 1] = line1[i][j]
                    continue
                elif j == len(line1[i]) - 1:
                    lines_2[-1] = line2[i][j]
                    continue
                elif not lines_2:
                    line1[i][j + 1] = line1[i][j]
                    continue
                else:
                    if line1[i][j] - lines_2[-1] >= line1[i][j + 1] - line2[i][j]:
                        line1[i][j + 1] = line1[i][j]
                        continue
                    elif line1[i][j] - lines_2[-1] >= line1[i][j + 1] - line2[i][j]:
                        lines_2[-1] = line2[i][j]
                        line1[i][j] = lines_1[-1]
                        continue
            else:
                lines_1.append(line1[i][j])
                lines_2.append(line2[i][j])
        line_1.append(lines_1)
        line_2.append(lines_2)

    pic4 = []
    for i in range(len(pic2)):
        pic5 = pic2[i]
        pic6 = []
        for j in range(len(line_1[i][:])):
            pic6.append(pic5[:, line_1[i][j]:line_2[i][j]])
        pic4.append(pic6)
    # 绘图
    pics = []
    for i in range(len(pic4)):
        for j in range(len(pic4[i])):
            pics.append(Image.fromarray(pic4[i][j].astype('uint8')))

    images = []
    for i in range(len(pics)):
        pic = pics[i].convert('L')
        pic = pic.resize((220, 480))
        pic_array = np.asarray(pic).copy()
        images.append(pic_array)
    for i in range(len(images)):
        if np.sum(images[i] < 200) / images[i].size < 0.05:
            # print(np.sum(images[i] < 200))
            # print(images[i].size)
            if i == len(images) - 1:
                del images[i]
            else:
                images[i] = images[i + 1]
    images = np.asarray(images)
    return images


if __name__ == '__main__':
    images_all = [np.full((220, 480), 255)]
    u = -1
    for ID_num in range(1, 2):
        u = u + 1
        print(u)
        picture_path = r"图片\女书图片\%d.jpg" % ID_num  # 合并路径得到图像的绝对路径
        images = process_image(picture_path)
        # print(np.abs(images_all[0] - images[0]).sum())
        if any(np.abs(arr - images[0]).sum() < 3000000 for arr in images_all):
            if len(images) == 1:
                images_all.append(images[0])
                image = Image.fromarray(images[0].astype('uint8'))
                image.save(r"图片\女书_new\%d.jpg" % ID_num)
            else:
                images_all.append(images[1])
                image = Image.fromarray(images[1].astype('uint8'))
                image.save(r"图片\女书_new\%d.jpg" % ID_num)
        else:
            images_all.append(images[0])
            image = Image.fromarray(images[0].astype('uint8'))
            image.save(r"图片\女书_new\%d.jpg" % ID_num)
