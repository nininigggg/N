import time

from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = "aaaa"


    def fake_conditions():
        print("当前时间为", time.time())


    WebDriverWait(driver, 10, 2).until(fake_conditions(), "hogwartz")

