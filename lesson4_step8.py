from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def calc(x):
    from math import log, sin
    return str(log(abs(12 * sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    browser.execute_script("window.scrollBy(0, 120);")
    browser.find_element(By.ID, "answer").send_keys(calc(
        browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(10)
    browser.quit()
