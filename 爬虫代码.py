import csv
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(executable_path="./chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://y.qq.com/n/ryqq/songDetail/004CGwK02ZhJ3u")
actions = ActionChains(driver)
driver.execute_script("window.scrollBy(0,5000)")

time.sleep(5)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,7000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,7000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,5000)")
time.sleep(5)
comments = []
times = []
zans=[]
a = driver.find_elements(By.CSS_SELECTOR,".comment__text span")
time_elements= driver.find_elements(By.CSS_SELECTOR,"[class='comment__date c_tx_thin']")
zan_elements=driver.find_elements(By.CSS_SELECTOR,".comment__zan")
for comment_element, time_element,zan_element in zip(a, time_elements,zan_elements):
    comment = comment_element.text
    time = time_element.text
    zan=zan_element.text
    comments.append(comment)
    times.append(time)
    zans.append(zan)
# 打印评论和时间信息
for comment, time in zip(comments, times):
    print(f"评论：{comment}")
    print(f"时间：{time}")
    print()
csv_file_path = 'data.csv'

# 使用CSV模块将数据写入CSV文件



print(len(a))

with open(csv_file_path, mode='w', newline='',encoding='utf-8') as file:

    writer = csv.writer(file)
    writer.writerow(['Comment', 'Time','zan'])  # 写入表头
    writer.writerows(zip(comments, times,zans))

driver.quit()