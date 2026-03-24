from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)

driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(3)

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)



mens = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class = 'desktop-navLink'])[1]")))
action.move_to_element(mens).perform()
sleep(2)



# driver.find_element(By.XPATH, "//a[text() = 'T-Shirts']").click()
ele = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[text() = 'T-Shirts'])[1]")))
ele.click()
sleep(2)



pic = wait.until(EC.presence_of_element_located((By.XPATH, "(//picture[@class='img-responsive'])[20]")))
action.move_to_element(pic).perform()
sleep(3)

driver.quit()
