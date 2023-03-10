from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    element = browser.find_element(By.ID, 'answer')
    element.send_keys(y)

    element = browser.find_element(By.ID, 'robotCheckbox')
    element.click()

    element = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    element.click()

    element = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()