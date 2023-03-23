
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys("New York")
#search_bar.send_keys(Keys.Return)
driver.maximize_window()
time.sleep(10)



