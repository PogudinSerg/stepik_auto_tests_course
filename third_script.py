import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log


driver = webdriver.Chrome()
time.sleep(5)
driver.get("http://suninjuly.github.io/redirect_accept.html")
time.sleep(5)
button = driver.find_element(By.CLASS_NAME, "trollface")
button.click()
window = driver.window_handles[1]
driver.switch_to.window(window)
x = driver.find_element(By.ID, "input_value").text
formula = log(abs(12*sin(int(x))))
driver.find_element(By.ID, "answer").send_keys(formula)
submit_btn = driver.find_element(By.CLASS_NAME, "btn")
submit_btn.click()


driver.quit()
