import time

from selenium.webdriver.common.by import By
from web_test.log_utils import logger
from web_test.base import Base


class TestRecord(Base):
    def test_login(self):
        # 登陆默认有输入值，首先清空输入值
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        time.sleep(10)


