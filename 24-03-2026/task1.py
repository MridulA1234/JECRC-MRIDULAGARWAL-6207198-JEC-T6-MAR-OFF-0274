from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome = webdriver.Chrome()
chrome.get("https://codepen.io/gdw96/pen/jOypoYL")
chrome.maximize_window()
time.sleep(3)

chrome.switch_to.frame("result")

user_field = chrome.find_element(By.ID, "username")
user_field.clear()
user_field.send_keys("testuser")

pass_field = chrome.find_element(By.ID, "password")
pass_field.clear()
pass_field.send_keys("testpass")

toggle_btn = chrome.find_element(By.ID, "showPsswd")
act = ActionChains(chrome)
act.click_and_hold(toggle_btn).perform()
time.sleep(3)
act.release().perform()

chrome.find_element(By.CLASS_NAME, "submit").click()
time.sleep(5)

chrome.back()
chrome.switch_to.frame("result")

heading = chrome.find_element(By.TAG_NAME, "h1").text
assert "Registration" in heading, "Heading not found on page."
print("Done")

chrome.quit()
