def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源准备：teardown module")


def test_case1():
    print("case1")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源准备：teardown function")


class TestDemo:
    def setup_class(self):
        print("资源准备：setup class")

    def teardown_class(self):
        print("资源准备：teardown class")

# 方法执行前后的准备
    def setup(self):
        print("资源准备：TestDemo setup ")

    def teardown(self):
        print("资源准备：TestDemo teardown ")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")