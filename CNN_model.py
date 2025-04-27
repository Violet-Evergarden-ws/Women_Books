import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import tensorflow as tf
import keras
from tensorflow.keras import losses, optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import MultiLabelBinarizer


# 数据处理
def data_process(image_array):
    image_array = image_array.reshape((image_array.shape[0], image_array.shape[1], 1))
    # 归一化
    image_array = image_array.astype('float32')
    image_array = image_array / 255
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
    # 定义输入形状，与x_train的维度(不包括样本数)一致
    input_shape = (480, 220, 1)
    # 创建Sequential模型
    model = Sequential()
    # 第一层卷积
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # 第二层卷积
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # 展平层，将卷积层的输出展平
    model.add(Flatten())
    # 添加全连接层
    model.add(Dense(256, activation='relu'))
    # 输出层，根据y_train的维度设置节点数
    # 如果是多分类问题，使用softmax激活函数
    # 如果是回归问题，则不需要激活函数或使用linear
    model.add(Dense(1717, activation='softmax'))  # 假设是多分类问题

    # 编译模型
    model.compile(optimizer=optimizers.Adam(),
                  loss=losses.CategoricalCrossentropy(from_logits=False),
                  metrics=['accuracy'])
    # 打印模型结构
    model.summary()

    # 训练模型
    model.fit(x_train,y_train,
              batch_size=32,
              epochs=20,
              verbose=1,
              validation_data=(x_test, y_test))

    # 保存模型
    print("保存模型中...")
    model.save('model_CNN.h5')
    print("保存成功！！")

    # 评估模型
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    return model

if __name__ == '__main__':
    X_train, Y_train, X_test, Y_test = load_data()
    print("训练集X纬度：", X_train.shape)
    print("训练集Y纬度：", Y_train.shape)
    print("测试集X纬度：", X_test.shape)
    print("测试集Y纬度：", Y_test.shape)
    model_CNN = create_model(X_train, Y_train, X_test, Y_test)