from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 使用官方的expected_conditions
    ele1 = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "#success_btn")))
    # driver.find_element(By.CSS_SELECTOR, "#success_btn").click()
    ele2 = driver.find_element(By.CSS_SELECTOR, "#success_btn")
    print(ele1, ele2)


if __name__ == '__main__':
    wait_until()
