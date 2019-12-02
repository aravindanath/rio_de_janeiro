import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")


def test_method1(setUp):
    print("Method one")


def test_method2(setUp):
    print("Method two")

#  py.test -v -s