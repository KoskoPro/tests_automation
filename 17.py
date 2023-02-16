from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/redirect_accept.html"
webrowser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    webrowser.get(link)
    webrowser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    new_window = webrowser.window_handles[1]
    webrowser.switch_to.window(new_window)
    y = calc(webrowser.find_element(By.ID, 'input_value').text)

    webrowser.find_element(By.ID, 'answer').send_keys(y)
    webrowser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    webrowser.quit()
