import pytest


def double(a):
    return a * 2


@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)


@pytest.mark.minus
def test_double_minus():
    print("test double minus")
    assert -2 == double(-1)


@pytest.mark.float
def test_double_float():
    print("test double float")
    assert 2.0 == double(1.0)
