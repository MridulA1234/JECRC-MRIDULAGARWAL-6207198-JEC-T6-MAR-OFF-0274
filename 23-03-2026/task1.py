from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = opts)

driver.get("https://www.royalchallengers.com/")
driver.maximize_window()
sleep(3)


img = driver.find_element(By.XPATH, "(//span[@class='prod-img'])[2]")
action = ActionChains(driver)
action.scroll_to_element(img).perform()
sleep(3)

for i in range(5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(1)

driver.quit()
