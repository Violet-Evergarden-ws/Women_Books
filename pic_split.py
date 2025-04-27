import Image_process as impro
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    img_path = r'图片/测试图片/t11.png'
    img = Image.open(img_path)
    img = img.convert('L')
    img = img.resize((500, 500))
    img = np.asarray(img).copy()
    (r, l) = img.shape
    print(img)
    