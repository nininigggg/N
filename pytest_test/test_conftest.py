import pytest


# 定义的登陆fixture避免用test开头
@pytest.fixture(scope="session", autouse=True)
def login():
    # setup
    print("登陆操作")
    token = "1234567890"
    username = "nnn"
    # teardown
    yield token, username
    print("登出操作")

@pytest.fixture()
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")
