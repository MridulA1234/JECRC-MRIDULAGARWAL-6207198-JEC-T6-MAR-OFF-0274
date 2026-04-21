from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://demoqa.com/alerts")
browser.maximize_window()
time.sleep(3)

browser.find_element(By.ID, "alertButton").click()
time.sleep(3)
simple_alert = browser.switch_to.alert
simple_alert.accept()

browser.find_element(By.ID, "timerAlertButton").click()
time.sleep(8)
timer_alert = browser.switch_to.alert
timer_alert.accept()
time.sleep(3)

browser.find_element(By.ID, "confirmButton").click()
time.sleep(3)
confirm_alert = browser.switch_to.alert
confirm_alert.accept()

confirm_text = browser.find_element(By.ID, "confirmResult").text
assert "Ok" in confirm_text, "Cancel was clicked instead"
print("ok")
time.sleep(3)

browser.find_element(By.ID, "promtButton").click()
time.sleep(3)
prompt_alert = browser.switch_to.alert
prompt_alert.send_keys("Selenium")
prompt_alert.accept()

prompt_text = browser.find_element(By.ID, "promptResult").text
assert "Selenium" in prompt_text, "Input text did not match"
print("ok")
time.sleep(3)

browser.quit()
