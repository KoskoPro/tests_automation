import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

answer = math.log(int(time.time()))
links = ['https://stepik.org/lesson/236895/step/1', \
         'https://stepik.org/lesson/236896/step/1', \
         'https://stepik.org/lesson/236897/step/1', \
         'https://stepik.org/lesson/236898/step/1', \
         'https://stepik.org/lesson/236899/step/1', \
         'https://stepik.org/lesson/236903/step/1', \
         'https://stepik.org/lesson/236904/step/1', \
         'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.ID, 'id_login_email').send_keys('####@gmail.com')
    browser.find_element(By.NAME, "password").send_keys('####')
    browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()
    time.sleep(5)

    try:
        browser.find_element(By.CSS_SELECTOR, 'button.again-btn').click()
        browser.find_element(By.CSS_SELECTOR, '.modal-popup__footer>button').click()
        time.sleep(2)
    except:
        answer = math.log(int(time.time()))
        browser.find_element(By.CLASS_NAME, 'string-quiz__textarea').send_keys(answer)
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        correct = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        assert correct == 'Correct!', 'wrong answer'
