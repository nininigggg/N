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
        # time.sleep(10)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-input__inner').send_keys("新增商品测试")
        button = self.driver.find_element(By.CSS_SELECTOR, '.dialog-footer .el-button--primary')
        # 添加显示等待位置
        time.sleep(3)
        button.click()
        time.sleep(1)
        res = self.driver.find_element(By.XPATH, "//*[text()='新增商品测试']")
        assert res != []
