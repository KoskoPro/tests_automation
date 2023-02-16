from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    y = calc(int(x_element))
    browser.find_element(By.ID,"answer").send_keys(y)
    browser.find_element(By.ID,"robotCheckbox").click()
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()