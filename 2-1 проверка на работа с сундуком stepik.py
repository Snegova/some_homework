import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    sunduk = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_element = int(sunduk.get_attribute("valuex"))
    x = x_element
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    time.sleep(5)
    browser.quit()


