from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import shutil

CHROMEDRIVER_PATH = "/usr/bin/chromedriver" 

DOWNLOAD_DIR = "/home/user/data"
TARGET_FILENAME = "samsung.csv"

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
driver.get("http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd")
time.sleep(2)

driver.get("http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0101020001")
time.sleep(2)

driver.execute_script("MDCSTAT.search('K');")
time.sleep(2)

search_input = driver.find_element(By.ID, "searchText0")
search_input.send_keys("삼성전자")
time.sleep(2)

search_btn = driver.find_element(By.ID, "jsSearchStock")
search_btn.click()
time.sleep(2)

driver.find_element(By.ID, "jsSearchPeriodType1Y").click()
time.sleep(2)
driver.find_element(By.ID, "jsSearchBtn").click()
time.sleep(2)
driver.find_element(By.ID, "jsDownBtn").click()
time.sleep(2) 

for fname in os.listdir(DOWNLOAD_DIR):
    if fname.endswith(".csv"):
        src = os.path.join(DOWNLOAD_DIR, fname)
        dst = os.path.join(DOWNLOAD_DIR, TARGET_FILENAME)
        shutil.move(src, dst)
        break

driver.quit()
print(f"[완료] {TARGET_FILENAME} 파일 저장됨: {DOWNLOAD_DIR}")
