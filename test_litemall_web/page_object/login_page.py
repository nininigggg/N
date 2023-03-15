"""登陆页面"""
from selenium.webdriver.common.by import By

from test_litemall_web.page_object.base_page import BasePage
from test_litemall_web.utils.log_utils import logger


class LoginPage(BasePage):
    _BASE_URL = "https://litemall.hogwarts.ceshiren.com/#/login"
    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BIN_LOGIN = (By.CSS_SELECTOR, ".el-button--primary")
    """登录页面：用户登录"""

    def login(self):
        # 访问登录页
        logger.info("访问登陆页")

        # 输入“用户名”
        self.do_send_keys("manage", self.__INPUT_USERNAME)
        # 输入“密码”
        self.do_send_keys("manage123", self.__INPUT_PASSWORD)
        # 点击“登录”按钮
        self.do_find(self.__BIN_LOGIN).click()
        # ==》首页
        from test_litemall_web.page_object.home_page import HomePage
        return HomePage(self.driver)
