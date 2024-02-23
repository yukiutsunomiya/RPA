# coding: utf-8
# ライブラリ読み込み
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = browser = webdriver.Chrome()

#ページ接続
driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=s-m8E43DZEe2NiaVXDtXUM9WON_2Pv5IjKCEOnldEFtUNUtOV0dSNUJIUkFURlVaT1FIQkdFMzM0NCQlQCN0PWcu')
time.sleep(15)
driver.find_element(By.ID, "i0116").send_keys("2410425@vsn.co.jp")
driver.find_element(By.ID,"idSIButton9").click()
time.sleep(10)
driver.find_element(By.ID, "i0118").send_keys("Kansai1425")
driver.find_element(By.ID,"idSIButton9").click()
time.sleep(5)
driver.find_element(By.ID,"idSIButton9").click()
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[1]/div[2]/div/span/input').send_keys("2410425")
driver.execute_script('arguments[0].setAttribute("type", "text");', driver.find_element(By.XPATH, '//*[@id="question-list"]/div[2]/div[2]/div/span/input'))
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[2]/div[2]/div/span/input').send_keys("宇都宮　祐樹")
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[3]/div[2]/div/div/div').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[4]/div[2]/div/div[1]/div[1]/div/label/span[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[5]/div[2]/div/div/div').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]').click()
driver.execute_script('arguments[0].setAttribute("type", "text");', driver.find_element(By.XPATH, '//*[@id="question-list"]/div[6]/div[2]/div/span/input'))
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[6]/div[2]/div/span/input').send_keys("Java SE Gold")
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[7]/div[2]/div/div/div/div/div/i').click()
driver.find_element(By.XPATH, '//*[@id="DatePicker-Callout1"]/div/div/div[2]/div[2]/div[1]/div/button[2]/i').click()
time.sleep(12)
driver.find_element(By.XPATH, '//*[@id="DatePicker-Callout1"]/div/div/div[2]/div[2]/div[1]/div/button[2]/i').click()
driver.find_element(By.XPATH, '//*[@id="DatePicker-Callout1"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[7]/button').click()
driver.execute_script('arguments[0].setAttribute("type", "text");', driver.find_element(By.XPATH, '//*[@id="question-list"]/div[8]/div[2]/div/span/input'))
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[8]/div[2]/div/span/input').send_keys("20%")
driver.execute_script('arguments[0].setAttribute("type", "text");', driver.find_element(By.XPATH, '//*[@id="question-list"]/div[9]/div[2]/div/span/input'))
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[9]/div[2]/div/span/input').send_keys("Java SE Goldの黒本の問題集を解きました。")
driver.execute_script('arguments[0].setAttribute("type", "text");', driver.find_element(By.XPATH, '//*[@id="question-list"]/div[10]/div[2]/div/span/textarea'))
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[10]/div[2]/div/span/textarea').send_keys(
    "09:00：勤務開始レポート作成" + Keys.ENTER +
    "09:15：Java Gold資格のため黒本の問題集の実施" + Keys.ENTER +
    "10:00：朝礼" + Keys.ENTER +
    "10:30：Java Gold資格のため黒本の問題集の実施" + Keys.ENTER +
    "12:00：昼休憩" + Keys.ENTER +
    "13:00：Java Gold資格のため黒本の問題集の実施" + Keys.ENTER +
    "16:00：夕礼" + Keys.ENTER +
    "16:30：Java Gold資格のため黒本の問題集の実施" + Keys.ENTER +
    "17:45：勤務終了レポート作成"
    )
driver.execute_script('arguments[0].setAttribute("type", "text");', driver.find_element(By.XPATH, '//*[@id="question-list"]/div[11]/div[2]/div/span/textarea'))
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[11]/div[2]/div/span/textarea').send_keys(
    "本日はJava Goldの黒本の問題集を解きました。" + Keys.ENTER +
    "クラスとインスターフェースに関する問題を解く際に、インナークラスの概念を理解しないといけないと思いました。"
    )
driver.find_element(By.XPATH, '//*[@id="question-list"]/div[12]/div[2]/div/div/div[1]/div/label/span[1]/input').click()
driver.find_element(By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button').click()

time.sleep(10)
driver.close()
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