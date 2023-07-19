import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import sin, log

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = driver.find_element(By.ID, "book")
button.click()
x = driver.find_element(By.ID, "input_value").text
formula = log(abs(12*sin(int(x))))
driver.find_element(By.ID, "answer").send_keys(formula)
submit_btn = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "solve")))
submit_btn.click()
time.sleep(1)
alert = driver.switch_to.alert
print(alert.text)



driver.quit()
