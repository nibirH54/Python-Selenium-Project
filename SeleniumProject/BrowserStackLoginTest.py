from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.browserstack.com/")
driver.maximize_window()

sign_in_button = driver.find_element(By.XPATH, '//a[@title="Sign In"][1]').click()

email_textbox = driver.find_element(By.ID, 'user_email_login')
email_textbox.send_keys('info@scratchtechsolutions.com')

password_textbox = driver.find_element(By.ID, 'user_password')
password_textbox.send_keys('Surma2009?')
click_on_signIn = driver.find_element(By.XPATH, '//input[@type="submit"][1]').click()
time.sleep(10)