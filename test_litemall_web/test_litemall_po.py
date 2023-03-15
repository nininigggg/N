import pytest

from test_litemall_web.page_object.login_page import LoginPage


class TestLitemall:
    # 前置动作
    def setup_class(self):
        """登录页面：用户登录"""
        self.home = LoginPage().login()

    def teardown_class(self):
        self.home.do_quit()

    # 新增功能
    # 优化三：参数化
    @pytest.mark.parametrize("category_name", ["001", "002"])
    def test_add_type(self, category_name):
        list_page = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name) \
            # 优化一：断言
        res = list_page.get_operate_result()
        assert "创建成功" == res
        # 优化二：数据清理
        list_page.delete_category(category_name)

    @pytest.mark.parametrize("category_name", ["004", "005"])
    def test_delete_type(self, category_name):
        res = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name) \
            .delete_category(category_name) \
            .get_delete_result()

        assert "删除成功" == res
# 优化五：生成测试报告
# pytest test_litemall_po.py -v -s --alluredir=./result
# allure serve ./result
