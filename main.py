import math
import time

import selenium.webdriver.chrome.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

link = "https://suninjuly.github.io/explicit_wait2.html"


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


def solve_captcha(driver: selenium.webdriver.chrome.webdriver.WebDriver):
    x_element = driver.find_element(By.ID, 'input_value')
    ans = calc(x_element.text)

    driver.find_element(By.ID, 'answer').send_keys(ans)

    driver.find_element(By.ID, 'solve').click()


if __name__ == '__main__':
    with webdriver.Chrome() as browser:
        browser.get(link)

        WebDriverWait(browser, 12).until(
            expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '100')
        )

        button = browser.find_element(By.ID, 'book')
        button.click()

        solve_captcha(browser)

        time.sleep(7)
