import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login_ui():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(5)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(5)
    driver.find_element(By.ID, "login-button").click()
    element = driver.find_element(By.CLASS_NAME,"app_logo")
    return element.is_displayed()

def login_invalid_ui():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys("sfsdfs")
    time.sleep(5)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(5)
    driver.find_element(By.ID, "login-button").click()
    element = driver.find_element(By.CLASS_NAME,"error-message-container error")
    return element.is_displayed()
