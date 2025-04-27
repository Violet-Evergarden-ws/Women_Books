import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import keras
import joblib


# 数据处理
def data_process(image_array):
    image_array = image_array.reshape((image_array.shape[0], image_array.shape[1], 1))
    # 归一化
    image_array = image_array.astype('float32')
    image_array = image_array / 255
    image_array = image_array.reshape(480 * 220)
    return image_array


# 导出图片数据与类别标签
def load_data():
    images_path = r"图片\女书_new"
    images_file = os.walk(images_path)
    images_list = []
    labels_list = []
    for root, dirs, files in images_file:
        for file in files:
            # 图片数据
            image_path = os.path.join(root, file)
            image_PIL = Image.open(image_path)
            image_PIL = image_PIL.resize((220, 480))
            image_PIL = image_PIL.convert('L')
            image_array = np.asarray(image_PIL).copy()
            image_array = data_process(image_array)
            images_list.append(image_array)

            # 类别标签
            word_ID = int(file.rstrip(".jpg"))
            # 将类向量（整数）转换为二进制类矩阵
            word_ID = keras.utils.to_categorical(word_ID, num_classes = 1717)
            labels_list.append(word_ID)
    images_list = np.asarray(images_list)
    labels_list = np.asarray(labels_list)

    # 划分训练集与测试集
    X_train = images_list
    Y_train = labels_list
    X_test = images_list[0:int(len(images_list)*0.3)]
    Y_test = labels_list[0:int(len(labels_list)*0.3)]
    return X_train, Y_train, X_test, Y_test


def create_model(x_train, y_train, x_test, y_test):
    knn = KNeighborsClassifier(n_neighbors=1)  # 选择邻居数量，这里选择了 3 作为示例
    knn.fit(x_train, y_train)

    # 保存模型
    joblib.dump(knn, "model_KNN.joblib")

    # 评估模型
    y_pred = knn.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    return knn

if __name__ == '__main__':
    X_train, Y_train, X_test, Y_test = load_data()
    print("训练集X纬度：", X_train.shape)
    print("训练集Y纬度：", Y_train.shape)
    print("测试集X纬度：", X_test.shape)
    print("测试集Y纬度：", Y_test.shape)
    model_CNN = create_model(X_train, Y_train, X_test, Y_test)