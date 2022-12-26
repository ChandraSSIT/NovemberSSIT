import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/register.php")

driver.implicitly_wait(10)

#  how to scroll
# scroll by pixel
# scroll till end
# scroll till element into view
time.sleep(5)
# scroll by pixel
# driver.execute_script("window.scrollBy(0,300)","")
# scroll till end of page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# scroll till element into view
element = driver.find_element(By.NAME, "address1")
driver.execute_script("arguments[0].scrollIntoView();", element)

#  to access data from dropdowns we should use Select option
select = Select(driver.find_element(By.NAME, "country"))
# select by index
# select.select_by_index(4)
# select by value
# select.select_by_value("BANGLADESH")
# select by visible text
select.select_by_visible_text("BASSA DE INDIA")
time.sleep(15)
# how can we execute javascript => by using execute script

# screen shot
#  how to capture screen shot
driver.get_screenshot_as_file("samplefilename.png")
driver.save_screenshot("image.jpg")

time.sleep(10)
# wait concepts
# mouse actions
# is selenium is asyncronous  => yes
#  how we will make it synchronous => how we will wait till element found
# wait concepts
# Implicit wait
# explicit wait

# Implicit  wait => this we will define at the page level , its dynamic wait, it will wait for 10 secs
#  to load all the elements in page
# explicit wait => this is based on condition for particular element based on condition
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located(driver.find_element(By.NAME,"country")))

# fluent wait
# we can define polling shamanism => for how many secs we need to verify once
# FluentWait<WebDriver>(driver)
# 			.withTimeout(30, TimeUnit.SECONDS)
# 			.pollingEvery(5, TimeUnit.SECONDS)

#  Action chains
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"txt1")).click().perform()
action.double_click(driver.find_element(By.ID,"txt2")).perform()
action.context_click(driver.find_element(By.ID,"tx3")).perform()
sourceelement = driver.find_element(By.ID,"element1")
targetelement = driver.find_element(By.ID,"element2")
action.drag_and_drop(sourceelement,targetelement).perform()

# Python,Rest API , APi Testing , Selenium

# Git hub , JIRA , Jenkins
# Git hub => its version control ,its open source
# svn,TFS(Team foundation server),Github

# source tree
# github for desktop 
