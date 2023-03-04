from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
lang = driver.find_element(By.ID, "langSelect-EN")
lang.click()
time.sleep(5)
big_button = driver.find_element(By.CSS_SELECTOR, "div button")
while True:
    time.sleep(0.3)
    big_button.click()
