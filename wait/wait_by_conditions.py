import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def muliti_click(target_element, next_element):
    def _inner(driver):
        driver.find_element(*target_element).click()
        return driver.find_element(*next_element)

    return _inner


# return对象，不是方法inner()


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 官方的expected_conditions无法满足需求
    # 自己缝状期望条件：一直点击按钮直到下一个页面出现
    WebDriverWait(driver, 10).until(
        muliti_click(
            (By.ID, "primary_btn"),
            (By.XPATH, "//*[text()='该弹窗点击两次后才会弹出']")
        ))
    time.sleep(3)


if __name__ == '__main__':
    wait_until()
