import pytest
import sys


@pytest.mark.skip
def test_aaa():
    print("代码未完成")
    assert True


@pytest.mark.skip(reason="代码未实现")
def test_bbb():
    assert False


def check_login():
    return False


def test_function():
    print("start")

    if not check_login():
        pytest.skip("unsupported configuration")
    print("end")


print(sys.platform)


@pytest.mark.skipif(sys.platform == 'darwin', reason="dose not run on mac")
def test_case1():
    assert True


@pytest.mark.skipif(sys.platform == 'win', reason="dose not run on windows")
def test_case1():
    assert True


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_case1():
    assert True


@pytest.mark.xfail
def test_aaa():
    print("test_xfail 方法执行")
    assert 2 == 1


xfail = pytest.mark.xfail


@xfail(reason='bug 110')
def test_hello4():
    assert 0
