# coding: utf-8
# ライブラリ読み込み
import jpholiday
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = browser = webdriver.Chrome()

#ページ接続
if not jpholiday.is_holiday(datetime.date.today()):
    driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=s-m8E43DZEe2NiaVXDtXUM9WON_2Pv5IjKCEOnldEFtUNEJCS1Q0M1oxRjNSVktKVEJZQ1lWVUxFSyQlQCN0PWcu&fbclid=IwAR1jJxn0OZvRAMicyl_JXeCdSnwdx96uN7340TTh47VDbode_jSZ6gu4rkI')
    time.sleep(15)
    driver.find_element(By.ID, "i0116").send_keys("2410425@vsn.co.jp")
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(5)
    driver.find_element(By.ID, "i0118").send_keys("Kansai1425")
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(5)
    driver.find_element(By.ID,"idSIButton9").click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="question-list"]/div[1]/div[2]/div/span/input').send_keys("2410425")
    driver.execute_script('arguments[0].setAttribute("type", "text");', driver.find_element(By.XPATH, '//*[@id="question-list"]/div[2]/div[2]/div/span/input'))
    driver.find_element(By.XPATH, '//*[@id="question-list"]/div[2]/div[2]/div/span/input').send_keys("宇都宮　祐樹")
    driver.find_element(By.XPATH, '//*[@id="question-list"]/div[3]/div[2]/div/div/div').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="question-list"]/div[4]/div[2]/div/div/div').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="question-list"]/div[5]/div[2]/div/div/div').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]').click()
    driver.find_element(By.XPATH, '//*[@id="question-list"]/div[6]/div[2]/div/div/div').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="question-list"]/div[7]/div[2]/div/div[1]/div[1]/div/label/span[1]/input').click()
    driver.find_element(By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button').click()
    time.sleep(10)
    driver.close()
exit()

""""
#10秒終了を待つ
time.sleep(1000)
#画面キャプチャを取得
driver.save_screenshot('conoha.png')

#クロームの終了処理
driver.close()

#◆cmdでスクリプトの実行
#python automation.py
"""