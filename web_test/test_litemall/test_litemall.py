import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_test.log_utils import logger
from web_test.base import Base


# 可优化点：1、封装登陆，后续新增用例用@装饰器触发登陆
#         2、新增配删除

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

    def test_new_type(self):
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-input__inner').send_keys("新增商品测试1")
        # 方法一：强制等待
        # button =self.driver.find_element(By.CSS_SELECTOR, '.dialog-footer .el-button--primary')
        # time.sleep(3)
        # button.click()
        # 方法二：添加显示等待位置：等待按钮可点击.....目前未调试通过
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.element_to_be_clickable(
        #         (By.CSS_SELECTOR, '.dialog-footer .el-button--primary')))
        # self.driver.find_element(By.CSS_SELECTOR, '.dialog-footer .el-button--primary').click()
        # 方法三：调用 Selenium click 事件
        # ele = self.driver.find_element(By.CSS_SELECTOR, '.dialog-footer .el-button--primary')
        # self.driver.execute_script("arguments[0].click();", ele)
        # 方法四：ActionChains
        element = self.driver.find_element(By.CSS_SELECTOR, '.dialog-footer .el-button--primary')
        ActionChains(self.driver).move_to_element(element).click(element).perform()

        time.sleep(1)
        res = self.driver.find_element(By.XPATH, "//*[text()='新增商品测试1']")
        assert res != []

    def test_delete_type(self):
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-input__inner').send_keys("删除商品测试")
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, '.dialog-footer .el-button--primary')))
        ele.click()
        self.driver.find_element(By.XPATH, "//*[text()='删除商品测试']").click()
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//*[text()='删除商品测试']")))
        res = self.driver.find_element(By.XPATH, "//*[text()='删除商品测试']")
        assert res == []
