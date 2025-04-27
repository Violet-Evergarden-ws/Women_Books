import pandas as pd
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


def word_WBooks(words_input):
    # 拆分字符串word
    words = [word_one for word_one in words_input]
    WBooks_path = r"图片\女书_new"
    Word_path = r"表格\testtabl.xls"
    chinese_xls = pd.read_excel(Word_path, usecols=['ID', 'WordRaw'])
    images_word = []
    for word in words:
        words_ID = chinese_xls[chinese_xls['WordRaw'] == word]['ID']
        if words_ID.empty:
            image_word = Image.open(r"Image\empty.png")
            image_word = image_word.resize((50, 120))
            images_word.append(image_word)
        else:
            for word_ID in words_ID:
                image_word = Image.open(r"图片\女书_new\{}.jpg".format(word_ID))
                image_word = image_word.resize((50, 120))
                images_word.append(image_word)

    return images_word

def WBooks_word(file_path):
    # 加载模型
    # import CNN_model as cnn_model
    import KNN_model as knn_model
    import Image_process as impro
    # from keras.models import load_model
    import joblib
    model = joblib.load("model_KNN.joblib")
    images_wb = impro.split_image(file_path)
    images = []
    for i in range(len(images_wb)):
        images.append(knn_model.data_process(images_wb[i]))
    images = np.asarray(images)

    # 导入文字查找表
    Word_path = r"表格\testtabl.xls"
    chinese_xls = pd.read_excel(Word_path, usecols=['ID', 'WordRaw'])

    # 开始预测结果
    words = ""
    # 使用predict方法进行预测
    results = np.round(model.predict(images)).astype('int')
    for result in results:
        if np.sum(result) == 1:
            result_ID = np.where(result==1)[0][0]
            result_word = chinese_xls[chinese_xls['ID'] == result_ID]['WordRaw'].item()
        else:
            result_word = "[]"
        words += result_word

    return words

if __name__ == '__main__':
    file_path = r"图片\测试图片\屏幕截图 2024-03-29 105236.png"
    print(WBooks_word(file_path))