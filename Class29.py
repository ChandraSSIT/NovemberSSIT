# Selenium
# It's a Page object model framework
# Html page => DOM => Document object model
#  we will access this HTMl as object, and we will perform methods on this
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# locators
# ID
# Name
# Class
# Css Selector
# X Path

# ID

# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# time.sleep(5)
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# time.sleep(5)


# Name
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
time.sleep(5)

driver.find_element(By.ID,"login-button").click()

# CLASSNAME
# driver.find_element(By.CLASS_NAME,"submit-button btn_action").click()

# CSS Selector
# driver.find_element(By.CSS_SELECTOR," div.form_group:nth-child(2) #password").send_keys("password")

# XPATH
# Absolute Path => which will be used with single slash
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/form/input").click()
# it will find the element from root of the parent till the child found
# Relative Path
#  we will use double slash
# //div[@class='form_group'][1]/input
driver.find_element(By.XPATH,"//div[@class='form_group'][1]/input").click()

time.sleep(30)

# driver.close() # it will close the current tab/window

# driver.quit() #it will close all the tabs/windows in browser




