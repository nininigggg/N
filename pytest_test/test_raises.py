import pytest

if __name__ == '__main__':
    # 运行当前目录下所有符合规则的测试用例，包括子目录（test_*.py, *_test.py）
    pytest.main()
    # 运行某一条用例
    pytest.main(['test_param1.py::test_dkej', '-vs'])
    # 运行某个标签
    pytest.main(['test_param1.py', '-vs', '-m', 'dkej'])


def test_raise():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ValueError("value must be 0 or None")


def test_raise1():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type in ValueError
    assert exc_info.value.args[0] == "value must be 42"
