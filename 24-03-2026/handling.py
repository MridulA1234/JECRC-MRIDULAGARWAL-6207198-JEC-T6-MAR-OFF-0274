# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/javascript_alerts')
# driver.maximize_window()
# sleep(3)


# ## simple alert
# driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# sleep(5)


# ## confirmation alert
# driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# sleep(2)

# driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.dismiss()
# sleep(5)

# ## prompt alert
# driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys('qwerty')
# alert.accept()
# sleep(5)

# driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys('qwerty')
# sleep(2)
# alert.dismiss()
# sleep(2)



# # from time import sleep
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# #
# # driver= webdriver.Chrome()
# # driver.get('https://the-internet.herokuapp.com/windows')
# # driver.maximize_window()
# # sleep(3)
# # parent_window=driver.current_window_handle
# # driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
# # sleep(2)
# # all_windows= driver.window_handles
# # print(len(all_windows))
# #
# # driver.switch_to_window(all_windows[-1])
# #
# # # print(driver.find_element(By.CLASS_NAME, 'example').text)
# # print(driver.current_window_handle)
# # assert 'New' in driver.find_element(By.CLASS_NAME, 'example').text
# # print('done')
# #
# # driver.close() ##
# # driver.close() ## it will close the current tab but not transfer the control so we need to do it by switching
# # driver.switch_to.window(parent_window)
# #
# #
# # driver.quit()

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/windows')
# driver.maximize_window()
# sleep(3)

# ## this open new website in same tab
# driver.get('https://www.google.com/')
# sleep(3)


# ## Opening a website in new tab
# driver.switch_to.new_window('tab')
# driver.get('https://www.google.com/')
# sleep(3)

# ## Opening a website in new window
# driver.switch_to.new_window('window')
# driver.get('https://www.google.com/')
# sleep(3)


# ## Opening a website in new tab
# driver.switch_to.new_window('tab')
# driver.get('https://www.google.com/')
# sleep(3)
