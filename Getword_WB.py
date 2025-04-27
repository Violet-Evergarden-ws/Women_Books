from selenium.webdriver.common.by import By
from selenium import webdriver
import pymysql
import pandas as pd
from selenium.webdriver.common.keys import Keys
import os
import time


def get_db():
    # 创建数据库连接
    db = pymysql.connect(
        host="localhost",  # MySQL服务器地址
        user="root",  # 用户名
        password="664850myqc",  # 密码
        database="WomenBook"  # 数据库名称
    )
    return db


def export_data(db, a):
    cursor = db.cursor()
    sql = "select Wordraw from wordrawtabl WHERE ID = " + str(a) + ""
    wordRaw = pd.read_sql(sql, con=db)
    return wordRaw


def insert(db, id, WordRaw, Womenbook_raw):
    cursor = db.cursor()    #定义游标
    sql = "INSERT INTO TestTabl_copy1(ID,WordRaw,WordWB) VALUES(" + str(id) + ",'" + WordRaw + "','"+ Womenbook_raw +"')"  # 设计数据库
    cursor.execute(sql)
    db.commit()


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get('https://nushuscript.org/nsbzz/')
    input_Chinese = driver.find_element(By.XPATH, "//*[@id='inputArea']")
    n = 12473
    for i in range(12608, 15629):
        words_raw = [one for one in str(export_data(get_db(), i))]
        words_raw2 = []
        for j in range(len(words_raw)):
            if words_raw[j] not in [' ', '：', '。', '，', '！', 'n', '—', '？', '…', '、', '“', '”', '.', '//', '\\', '·',
                                    '~', '、', '《', '》', '|', '；', '\n', 'W', 'o', 'r', 'd', 'R', 'a', 'w', '0']:
                words_raw2.append(words_raw[j])
        input_Chinese.send_keys(str(words_raw2[0]))
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/form/p[2]/input").click()
        try:
            Womenbook_raw = driver.find_element(By.XPATH, "//*[@id='outputArea']/img").get_attribute('src')
            insert(get_db(), n, str(words_raw2[0]), Womenbook_raw)
            n = n+1
            input_Chinese.send_keys(Keys.CONTROL, "a")
            input_Chinese.send_keys(Keys.BACK_SPACE)
        except Exception as e:
            continue
            input_Chinese.send_keys(Keys.CONTROL, "a")
            input_Chinese.send_keys(Keys.BACK_SPACE)
