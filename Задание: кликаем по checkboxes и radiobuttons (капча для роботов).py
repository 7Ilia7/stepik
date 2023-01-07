from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, '.form-group span:nth-child(2)')
    x = x_element.text
    y = calc(x)

    # element = browser.find_element(By.CSS_SELECTOR, '.form-control')
    # element.send_keys((calc(y)))

    # element = browser.find_element(By.ID, '#robotCheckbox')
    # element.click()
    #
    # element = browser.find_element(By.ID, '#robotsRule')
    # element.click()
    #
    # element = browser.find_element(By.ID, '.btn.btn-default')
    # element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()