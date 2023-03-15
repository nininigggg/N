"""列表页面"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from test_litemall_web.page_object.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait

from test_litemall_web.utils.log_utils import logger


class CategoryListPage(BasePage):
    __BTN_ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD_OPERATE = (By.XPATH, '//p[contains(text(), "创建")]')
    __MSG_DELETE_OPERATE = (By.XPATH, '//p[contains(text(), "删除")]')
    """类目列表页面：点击添加"""

    def click_add(self):
        # 优化四：添加日志
        logger.info("类目列表页面：点击添加")
        # 点击“添加”按钮
        self.do_find(self.__BTN_ADD).click()
        # ==》创建类目页面
        from test_litemall_web.page_object.category_creat_page import CategoryCreatPage
        return CategoryCreatPage(self.driver)

    """类目列表页面：获取操作结果"""

    def get_operate_result(self):
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_ADD_OPERATE)
        msg = element.text
        logger.info(f"冒泡消息是：{msg}")
        # ==》返回消息文本
        return msg

    def delete_category(self, category_name):
        # 对指定类目进行删除
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()
        # ==》当前页面
        return CategoryListPage(self.driver)

    def get_delete_result(self):
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_DELETE_OPERATE)
        msg = element.text
        logger.info(f"冒泡消息是：{msg}")
        # ==》返回消息文本
        return msg
