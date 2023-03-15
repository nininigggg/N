"""新增页面"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_litemall_web.page_object.base_page import BasePage
from test_litemall_web.utils.log_utils import logger
from test_litemall_web.utils.web_utils import click_exception


class CategoryCreatPage(BasePage):
    __INPUT_CATEGORY_NAME = (By.CSS_SELECTOR, '.el-input__inner')
    __BTN_CONFIRM = (By.CSS_SELECTOR, ".dialog-footer .el-button--primary")
    """创建类目页面：创建类目"""
    def create_category(self, category_name):
        logger.info("创建类目页面：创建类目")
        # 输入“类目名称”
        self.do_send_keys(category_name, self.__INPUT_CATEGORY_NAME)
        # 点击“确定”按钮
        WebDriverWait(self.driver, 10).until(click_exception(*self.__BTN_CONFIRM))
        # ==》类目列表页面
        from test_litemall_web.page_object.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)
