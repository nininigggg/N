import pytest

search_list = ['appium', 'selenium', 'pytest']


@pytest.mark.parametrize('name', search_list)
def test_search(name):
    assert name in search_list


@pytest.mark.parametrize('test_input,expected', [("3+5", 8), ("2+5", 7), ("7+5", 12)],
                         ids=['number1', 'number2', 'number3'])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("wd", ['appium', 'selenium', 'pytest'])
@pytest.mark.parametrize("code", ["utf-8", "gbk", "gb2312"])
def test_dkej(wd, code):
    print(f"wd:{wd}, code:{code}")

