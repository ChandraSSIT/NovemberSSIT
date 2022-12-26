import time

from selenium  import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("https://demo.guru99.com/test/radio.html")
genderoption = driver.find_element(By.CSS_SELECTOR,"[value='Option 1']")
genderoption.click()
print(genderoption.is_displayed())
print(genderoption.is_enabled())
print(genderoption.is_selected())

time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR,"[value='Option 2']")
element.click()

driver.find_element(By.CSS_SELECTOR,"[value='Option 1']").click()
# element.click()

# check boxes
driver.find_element(By.CSS_SELECTOR,"[value='checkbox1']").click()
driver.find_element(By.CSS_SELECTOR,"[value='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,"[value='checkbox3']").click()

time.sleep(10)
