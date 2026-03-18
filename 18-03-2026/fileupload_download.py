from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

######################################################

driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH, '//a[text()="Screenshot 2025-12-24 164603.png"]').click()
sleep(10)
print('downloaded')

driver.quit()
