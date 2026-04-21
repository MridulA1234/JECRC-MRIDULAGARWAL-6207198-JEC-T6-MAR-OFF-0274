from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()
chrome.get("https://demoqa.com/browser-windows")
chrome.maximize_window()
time.sleep(3)

parent_window = chrome.current_window_handle

chrome.find_element(By.ID, "tabButton").click()
opened_tabs = chrome.window_handles
chrome.switch_to.window(opened_tabs[-1])
tab_heading = chrome.find_element(By.ID, "sampleHeading").text
time.sleep(2)
assert "This is a sample page" in tab_heading, "Different"
print("Same")
chrome.close()
chrome.switch_to.window(parent_window)
time.sleep(3)

chrome.find_element(By.ID, "windowButton").click()
opened_windows = chrome.window_handles
chrome.switch_to.window(opened_windows[-1])
win_heading = chrome.find_element(By.ID, "sampleHeading").text
time.sleep(2)
assert "This is a sample page" in win_heading, "Different"
print("Same")
chrome.close()
chrome.switch_to.window(parent_window)
time.sleep(3)

chrome.find_element(By.ID, "messageWindowButton").click()
msg_windows = chrome.window_handles
chrome.switch_to.window(msg_windows[-1])
chrome.close()
chrome.switch_to.window(parent_window)
time.sleep(3)

chrome.quit()
