import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://www.mortgagecalculator.org/")
driver.maximize_window()

#Enter Home-value as $300000

driver.find_element(By.ID, "homeval").clear()
driver.find_element(By.ID, "homeval").send_keys("300000")

#Enter down-payment as $60000

driver.find_element(By.ID, "downpayment").clear()
driver.find_element(By.ID, "downpayment").send_keys("60000")

#Click on the radio button to select $ option

driver.find_element(By.NAME, "param[downpayment_type]").click()

#Enter loan-amount as $240,000

driver.find_element(By.ID, "loanamt").clear()
driver.find_element(By.ID, "loanamt").send_keys("240000")

#Enter interest rate as 3%

driver.find_element(By.ID, "intrstsrate").clear()
driver.find_element(By.ID, "intrstsrate").send_keys("3")

#Enter Loan Term as 30 Years

driver.find_element(By.ID, "loanterm").clear()
driver.find_element(By.ID, "loanterm").send_keys("30")

#Select the start month as April

select = Select(driver.find_element(By.NAME, "param[start_month]"))
select.select_by_visible_text("Apr")

#Enter the Year as 2023

driver.find_element(By.ID, "start_year").clear()
driver.find_element(By.ID, "start_year").send_keys("2023")

#Enter PropertyTax as $5000

driver.find_element(By.ID, "pptytax").clear()
driver.find_element(By.ID, "pptytax").send_keys("5000")

#Enter PMI AS 0.5

driver.find_element(By.ID, "pmi").clear()
driver.find_element(By.ID, "pmi").send_keys("0.5")

#Enter HOI as $1000

driver.find_element(By.ID, "hoi").clear()
driver.find_element(By.ID, "hoi").send_keys("1000")

#Enter Monthly HOA as $ 100

driver.find_element(By.ID, "hoa").clear()
driver.find_element(By.ID, "hoa").send_keys("100")

#Select loan type as FHA

select = Select(driver.find_element(By.NAME, "param[milserve]"))
select.select_by_visible_text("FHA")

#Select Buy option from the dropdown

select = Select(driver.find_element(By.NAME, "param[refiorbuy]"))
select.select_by_visible_text("Buy")

#Click on calcu;ate Button
driver.find_element(By.NAME, "cal").click()

expectedTotalMonthlyPayment = "1611.85"
formattedXpath = f"//h3[text()='$1,611.85']"

present = driver.find_element(By.XPATH, formattedXpath).is_displayed()

assert present, "Total Monthly Payment is not Presented"

time.sleep(10)

driver.quit()


