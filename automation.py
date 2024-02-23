
# coding: utf-8
# ライブラリ読み込み
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
"""
# chromedriver.exeのパスを指定
chromedriver_path = 'C:/chromedriver-win64/chromedriver.exe'

# chromedriverのサービスを作成
service = Service(chromedriver_path)

# クロームの立ち上げ
driver = webdriver.Chrome(service=service)
"""
# 以降のコードを続けて実行
from selenium import webdriver
 
driver = browser = webdriver.Chrome()
driver.get("https://www.yahoo.co.jp/")


#ページ接続
driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=s-m8E43DZEe2NiaVXDtXUM9WON_2Pv5IjKCEOnldEFtUNEJCS1Q0M1oxRjNSVktKVEJZQ1lWVUxFSyQlQCN0PWcu&fbclid=IwAR1jJxn0OZvRAMicyl_JXeCdSnwdx96uN7340TTh47VDbode_jSZ6gu4rkI')


##driver.find_element_by_class_name("-_S-56").send_keys("2410425")

##driver.find_element(By.CLASS_NAME, “class-name”)

#10秒終了を待つ
time.sleep(1000)

# 特定の要素をクラス名で見つける
element = driver.find_element_by_class_name("-_S-56")

# 要素に対してテキストを送信
element.send_keys("2410425")
""""
#画面キャプチャを取得
driver.save_screenshot('conoha.png')

#クロームの終了処理
driver.close()

#◆cmdでスクリプトの実行
#python automation.py
"""