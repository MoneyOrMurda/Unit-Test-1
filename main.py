from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

# Переходим на веб-сайт
driver.get("https://ya.ru")

search_box = driver.find_element(By.NAME, "text")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)

import time
time.sleep(5)

driver.quit()