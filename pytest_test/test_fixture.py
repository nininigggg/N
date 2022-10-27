import pytest


# 定义的登陆fixture避免用test开头
# @pytest.fixture(scope="module")
# def login():
#     # setup
#     print("登陆操作")
#     token = "1234567890"
#     # teardown
#     yield token
#     print("登出操作")


def test_search():
    print("搜索")


def test_cart(login, connectDB):
    print("购物车")
    print(login)


def test_order(login):
    print("下单")


class TestDemo:
    def test_case1(self, login):
        print("case1")

    def test_case2(self, login):
        print("case2")


# fixture 参数化
@pytest.fixture(params=[["selenium", 123], ["appium", 123456]])
def login(request):
    print(f"用户名：{request.param}")
    return request.param


def test_demo1(login):
    print(f"demo1 cse：数据为：{login}")
