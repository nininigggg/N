import time
from selenium.webdriver.common.by import By
from web_test.base import Base
from selenium.webdriver.support.wait import WebDriverWait


class TestWebdriverWait(Base):

    def test_webdriver_wait(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")

        # 解决的问题：有的按钮点击一次没有反应，可能要点击多次，比如企业微信的添加成员
        # 解决的方案：一直点击按钮，直到下个页面出现，封装成显式等待的一个条件
        def muliti_click(button_element, until_ele):
            # 函数封装
            def inner(driver):
                # 封装点击方法
                driver.find_element(By.XPATH, button_element).click()
                return driver.find_element(By.XPATH, until_ele)

            return inner

        time.sleep(5)
        # 在限制时间内会一直点击按钮，直到展示弹框
        WebDriverWait(self.driver, 10).until(
            muliti_click("//*[text()='点击两次响应']", "//*[text()='该弹框点击两次后才会弹出']"))
        time.sleep(5)
