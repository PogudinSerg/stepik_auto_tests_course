import time
from selenium import webdriver
from math import sin, log

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "btn-primary").click()
alert = driver.switch_to.alert
alert.accept()

x = driver.find_element(By.ID, "input_value").text
formula = log(abs(12*sin(int(x))))
driver.find_element(By.ID, "answer").send_keys(formula)
submit_btn = driver.find_element(By.CLASS_NAME, "btn")
# js_code = "arguments[0].scrollIntoView();"
# # Execute the JS script
# driver.execute_script(js_code, submit_btn)
#
# check_box = driver.find_element(By.ID, "robotCheckbox")
# check_box.click()
# radio_button = driver.find_element(By.ID, "robotsRule")
# radio_button.click()
submit_btn.click()
print()


# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()

