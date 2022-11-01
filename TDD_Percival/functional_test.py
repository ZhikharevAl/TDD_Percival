import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from packaging import version

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
base_url = "http://127.0.0.1:8000/"
driver.get(base_url)
title = driver.find_element(By.CSS_SELECTOR, 'a[class="logo"]').text
print(title)
assert title == "django"
print("Test passed")
