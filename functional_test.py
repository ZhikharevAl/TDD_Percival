import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from packaging import version

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
base_url = "https://localhost:8080"
time.sleep(2)
assert 'Django' in driver.title
