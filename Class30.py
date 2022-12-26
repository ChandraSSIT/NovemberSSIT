# Navigation commands
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.NAME, "user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(5)

driver.find_element(By.ID, "login-button").click()

time.sleep(2)
driver.find_element(By.ID, "item_4_title_link").click()
time.sleep(2)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
# Navigation commands
# back
# forward
# refresh

time.sleep(20)

# conditional commands
element = driver.find_element(By.ID, "sample")
element.is_enabled() # to check any element is enabled or not
element.is_selected() # to check whether element is selected ( we will use this for radio , check box)
element.is_displayed()  # to check particular element is visbile or not in page
